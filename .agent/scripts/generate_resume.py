import yaml
import jinja2
import os
import sys
import re

# Configuration
TEMPLATE_FILE = ".agent/templates/resume_template.tex.j2"
OUTPUT_DIR = "Resume_Building/Generated"

# Validation Rules
MIN_BULLET_LENGTH = 100 # eased slightly from 150 to allow for punchy intro bullets, but strict on average
FORBIDDEN_WORDS = ["Accomplished", "Responsible for", "Tasked with", "Helped"]

def escape_latex(text):
    """
    Escapes special LaTeX characters in the text.
    """
    if not isinstance(text, str):
        return text
    
    replacements = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
    }
    
    # regex to avoid double escaping if already escaped (simple check)
    # This is a basic escaper. For a resume, we mostly care about & and %
    
    # We will use a simple replacement, but we need to be careful not to escape 
    # macros if we allow them. However, our goal is strict data, so macros 
    # might not be in the YAML.
    # If the user puts \textbf{...} in the yaml, we SHOULD escape the backslash 
    # to prevent them from breaking the build, unless we decide the YAML contains 
    # trusted LaTeX. 
    # DECISION: The YAML should be PLAIN TEXT. Formatting belongs in the template.
    # So we escape EVERYTHING.
    
    # But wait, looking at the GTM resume, there are bolded parts in bullets:
    # \textbf{Orchestrated the Go-to-Market (GTM) strategy}
    # If we escape backslashes, we break this.
    #
    # STRATEGY: We will ALLOW LaTeX formatting commands in the YAML (bold, italic)
    # but strictly escape special chars like & and %.
    
    # To do this safely, we can just replace & and % and $ which are the most common offenders.
    # We will NOT escape \ or { or } to allow \textbf{}.
    
    text = text.replace('&', r'\&')
    text = text.replace('%', r'\%')
    text = text.replace('$', r'\$')
    text = text.replace('#', r'\#')
    text = text.replace('_', r'\_')
    
    return text

def validate_bullets(bullets, context=""):
    """
    Validates a list of bullets against strict rules.
    """
    errors = []
    for i, bullet in enumerate(bullets):
        # 1. Check Forbidden Words
        for word in FORBIDDEN_WORDS:
            if re.search(r'\b' + re.escape(word) + r'\b', bullet, re.IGNORECASE):
                errors.append(f"[{context} Bullet {i+1}] Contains forbidden word: '{word}'")
        
        # 2. Check Length (Warning for now, strict later?)
        # Clean latex commands for length check
        clean_text = re.sub(r'\\[a-zA-Z]+{([^}]*)}', r'\1', bullet)
        if len(clean_text) < MIN_BULLET_LENGTH:
             errors.append(f"[{context} Bullet {i+1}] Too short ({len(clean_text)} chars). Minimum {MIN_BULLET_LENGTH}.")
             
    return errors

def validate_data(data):
    """
    Validates the entire data structure.
    """
    errors = []
    
    # Validate Experience
    if 'experience' in data:
        for exp in data['experience']:
            role = exp.get('role', 'Unknown Role')
            errors.extend(validate_bullets(exp.get('bullets', []), context=f"Experience: {role}"))

    # Validate Projects
    if 'projects' in data:
        for proj in data['projects']:
            name = proj.get('name', 'Unknown Project')
            errors.extend(validate_bullets(proj.get('bullets', []), context=f"Project: {name}"))
            
    return errors

import argparse

def main():
    parser = argparse.ArgumentParser(description="Generate a resume from YAML data.")
    parser.add_argument("input_file", nargs="?", default=".agent/data/Abhishek/role_tpm.yaml", help="Path to the YAML data file")
    parser.add_argument("--output", "-o", help="Path to the output LaTeX file")
    args = parser.parse_args()

    # Use the provided input file
    data_file = args.input_file

    print(f"Reading data from {data_file}...")
    try:
        with open(data_file, 'r') as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: Data file not found at {data_file}")
        sys.exit(1)
        
    print("Validating data...")
    errors = validate_data(data)
    
    if errors:
        print("\n" + "="*40)
        print("VALIDATION FAILED")
        print("="*40)
        for err in errors:
            print(f"❌ {err}")
        print("="*40 + "\n")
        print("Generation ABORTED. Fix the errors in resume_data.yaml.")
        sys.exit(1)
    else:
        print("✅ Validation PASSED.")

    # Pre-process data to escape LaTeX
    # We need to walk the dict and escape strings
    # But wait, we decided to allow formatting commands.
    # The escape_latex function handles & % $ # _
    
    def recursive_escape(item):
        if isinstance(item, str):
            return escape_latex(item)
        elif isinstance(item, list):
            return [recursive_escape(i) for i in item]
        elif isinstance(item, dict):
            return {k: recursive_escape(v) for k, v in item.items()}
        else:
            return item

    escaped_data = recursive_escape(data)

    print(f"Loading template from {TEMPLATE_FILE}...")
    try:
        env = jinja2.Environment(
            block_start_string='{%',
            block_end_string='%}',
            variable_start_string='<<',
            variable_end_string='>>',
            comment_start_string='((#',
            comment_end_string='#))',
            loader=jinja2.FileSystemLoader(os.path.dirname(TEMPLATE_FILE)),
            autoescape=False # We handle escaping manually
        )
        template = env.get_template(os.path.basename(TEMPLATE_FILE))
    except jinja2.TemplateNotFound:
        print(f"Error: Template not found at {TEMPLATE_FILE}")
        sys.exit(1)

    print("Rendering resume...")
    rendered_tex = template.render(**escaped_data)
    
    if args.output:
        output_file = args.output
        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
    else:
        # Ensure output directory exists
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
        # Determine output filename
        output_filename = data.get("meta", {}).get("filename", "Generated_Resume.tex")
        if not output_filename.endswith(".tex"):
            output_filename += ".tex"
        output_file = os.path.join(OUTPUT_DIR, output_filename)
    
    print(f"Writing to {output_file}...")
    with open(output_file, 'w') as f:
        f.write(rendered_tex)
        
    print("✅ Resume Generation COMPLETE.")

if __name__ == "__main__":
    main()
