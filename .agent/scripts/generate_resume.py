import yaml
import jinja2
import os
import sys
import re
import subprocess
import shutil

# Configuration
TEMPLATE_FILE = ".agent/templates/resume_template.tex.j2"
OUTPUT_DIR = "Resume_Building/Generated"

# Validation Rules (Strict SKILL.md Compliance)
MIN_BULLET_LENGTH = 215 
MAX_BULLET_LENGTH = 245 # Optimized for 2-line visual symmetry
FORBIDDEN_WORDS = [
    "Accomplished", "Responsible for", "Tasked with", "Helped", 
    "Managed", "Participated", "Worked on", "Involved in", "Assisted"
]

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
    
    # STRATEGY: We will ALLOW LaTeX formatting commands in the YAML (bold, italic)
    # but strictly escape special chars like & and %.
    
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
                errors.append(f"[{context} Bullet {i+1}] Contains weak/forbidden word: '{word}'")
        
        # 2. Check Length (Strict SKILL.md 190-230 rule)
        # Clean latex commands for length check
        clean_text = re.sub(r'\\[a-zA-Z]+{([^}]*)}', r'\1', bullet)
        if len(clean_text) < MIN_BULLET_LENGTH:
             errors.append(f"[{context} Bullet {i+1}] Too short ({len(clean_text)} chars). Minimum {MIN_BULLET_LENGTH}.")
        if len(clean_text) > MAX_BULLET_LENGTH:
             errors.append(f"[{context} Bullet {i+1}] Too long ({len(clean_text)} chars). Maximum {MAX_BULLET_LENGTH}.")
             
        # 3. XYZ Check (Basic heuristic: must contain "by" and some metrics/keywords)
        # This is hard to do perfectly, but we can check for "by" as a proxy for 'How'
        if "by" not in bullet.lower() and "utilizing" not in bullet.lower() and "leveraging" not in bullet.lower():
            errors.append(f"[{context} Bullet {i+1}] Missing 'How' component (by/leveraging/utilizing). Does not follow XYZ.")

    return errors

def validate_dates(data):
    """
    Validates that dates use full month names.
    """
    errors = []
    short_months = ["Jan ", "Feb ", "Mar ", "Apr ", "Jun ", "Jul ", "Aug ", "Sep ", "Oct ", "Nov ", "Dec "]
    
    def check_value(val, context):
        if isinstance(val, str):
            for sm in short_months:
                if sm in val:
                    errors.append(f"[{context}] Date contains abbreviated month: '{sm.strip()}'")
        elif isinstance(val, list):
            for item in val:
                check_value(item, context)
        elif isinstance(val, dict):
            for k, v in val.items():
                check_value(v, f"{context} -> {k}")

    if 'education' in data:
        for i, edu in enumerate(data['education']):
            check_value(edu.get('dates', ''), f"Education {i+1} dates")
            if 'multi_degree' in edu:
                for j, md in enumerate(edu['multi_degree']):
                    check_value(md.get('dates', ''), f"Education {i+1} multi_degree {j+1} dates")

    if 'experience' in data:
        for i, exp in enumerate(data['experience']):
            check_value(exp.get('dates', ''), f"Experience {i+1} dates")

    if 'products' in data:
        for i, prod in enumerate(data['products']):
            check_value(prod.get('dates', ''), f"Product {i+1} dates")

    if 'projects' in data:
        for i, proj in enumerate(data['projects']):
            check_value(proj.get('dates', ''), f"Project {i+1} dates")

    return errors

def validate_data(data):
    """
    Validates the entire data structure.
    """
    errors = []
    
    # 1. Validate Dates (Full Month Names)
    errors.extend(validate_dates(data))
    
    # 2. Validate Experience
    if 'experience' in data:
        for exp in data['experience']:
            role = exp.get('role', exp.get('company', 'Unknown Role'))
            errors.extend(validate_bullets(exp.get('bullets', []), context=f"Experience: {role}"))

    # 3. Validate Products (New Structure)
    if 'products' in data:
        for prod in data['products']:
            name = prod.get('name', 'Unknown Product')
            errors.extend(validate_bullets(prod.get('bullets', []), context=f"Product: {name}"))

    # 4. Validate Projects
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
    parser.add_argument("--template", "-t", help="Path to a custom Jinja2 template file (overrides TEMPLATE_FILE and meta.template)")
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

    # Resolve template: CLI arg > meta.template in YAML > default TEMPLATE_FILE
    template_file = TEMPLATE_FILE
    if args.template:
        template_file = args.template
        print(f"Using custom template (CLI): {template_file}")
    elif data.get("meta", {}).get("template"):
        template_file = data["meta"]["template"]
        print(f"Using custom template (meta.yaml): {template_file}")

    print(f"Loading template from {template_file}...")
    try:
        env = jinja2.Environment(
            block_start_string='{%',
            block_end_string='%}',
            variable_start_string='<<',
            variable_end_string='>>',
            comment_start_string='((#',
            comment_end_string='#))',
            loader=jinja2.FileSystemLoader(os.path.dirname(template_file)),
            autoescape=False # We handle escaping manually
        )
        template = env.get_template(os.path.basename(template_file))
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
        # Determine output filename/path from metadata
        # The meta.filename in our YAMLs already contains the folder (e.g., Resume_Building/Abhishek/Product/...)
        output_path = data.get("meta", {}).get("filename", "Generated_Resume.tex")
        
        # If the filename contains path separators, it's already a structured path
        if "/" in output_path or "\\" in output_path:
            output_file = output_path
            output_dir = os.path.dirname(output_file)
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
        else:
            # Fallback to default OUTPUT_DIR if it's just a filename
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            if not output_path.endswith(".tex"):
                output_path += ".tex"
            output_file = os.path.join(OUTPUT_DIR, output_path)
    
    print(f"Writing to {output_file}...")
    with open(output_file, 'w') as f:
        f.write(rendered_tex)
        
    print("✅ Resume Generation COMPLETE.")
    compile_to_pdf(output_file)

def compile_to_pdf(tex_file):
    """
    Compiles a .tex file to PDF using pdflatex, then removes auxiliary files.
    Skips silently if pdflatex is not installed.
    """
    if not shutil.which("pdflatex"):
        print("⚠️  pdflatex not found on PATH — skipping PDF compilation.")
        print("   Run: eval \"$(/usr/libexec/path_helper)\" to activate TeX Live.")
        return

    tex_dir = os.path.dirname(os.path.abspath(tex_file))
    tex_name = os.path.basename(tex_file)
    base_name = os.path.splitext(tex_name)[0]

    print(f"Compiling {tex_name} to PDF...")
    result = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", tex_name],
        cwd=tex_dir,
        capture_output=True,
        text=True
    )

    # Clean up auxiliary files
    for ext in [".log", ".aux", ".out"]:
        aux_file = os.path.join(tex_dir, base_name + ext)
        if os.path.exists(aux_file):
            os.remove(aux_file)

    pdf_file = os.path.join(tex_dir, base_name + ".pdf")
    if result.returncode == 0 and os.path.exists(pdf_file):
        print(f"✅ PDF compiled: {pdf_file}")
    else:
        print("❌ PDF compilation failed. pdflatex output:")
        # Show only error lines to keep output clean
        for line in result.stdout.splitlines():
            if line.startswith("!") or "Error" in line:
                print(f"   {line}")

if __name__ == "__main__":
    main()
