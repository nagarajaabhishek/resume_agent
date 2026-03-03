import yaml
import jinja2
import os
import sys
import re
import argparse

# Configuration
TEMPLATE_FILE = ".agent/templates/cover_letter_template.tex.j2"
OUTPUT_DIR = "Resume_Building/Generated"

def escape_latex(text):
    """
    Escapes special LaTeX characters in the text.
    """
    if not isinstance(text, str):
        return text
    
    # We allow formatting commands like \textbf{}
    text = text.replace('&', r'\&')
    text = text.replace('%', r'\%')
    text = text.replace('$', r'\$')
    text = text.replace('#', r'\#')
    text = text.replace('_', r'\_')
    
    return text

def validate_cover_letter(data):
    """
    Validates the cover letter data.
    """
    errors = []
    if 'cover_letter' not in data:
        errors.append("Missing 'cover_letter' section in YAML.")
        return errors
        
    cl = data['cover_letter']
    required_fields = ['hook', 'bridge', 'evidence', 'close']
    for field in required_fields:
        if field not in cl or not cl[field]:
            errors.append(f"Missing cover letter field: '{field}'")
            
    # Check for placeholders
    placeholders = ["[Company Name]", "[Job Title]", "[", "]"]
    for field, content in cl.items():
        if isinstance(content, str):
            for p in placeholders:
                if p in content:
                    errors.append(f"Potential placeholder '{p}' found in field '{field}'.")
                    
    return errors

def main():
    parser = argparse.ArgumentParser(description="Generate a cover letter from YAML data.")
    parser.add_argument("input_file", help="Path to the YAML data file")
    parser.add_argument("--output", "-o", help="Path to the output LaTeX file")
    args = parser.parse_args()

    data_file = args.input_file

    print(f"Reading data from {data_file}...")
    try:
        with open(data_file, 'r') as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: Data file not found at {data_file}")
        sys.exit(1)
        
    print("Validating cover letter data...")
    errors = validate_cover_letter(data)
    
    if errors:
        print("\n" + "="*40)
        print("VALIDATION FAILED")
        print("="*40)
        for err in errors:
            print(f"❌ {err}")
        print("="*40 + "\n")
        print("Generation ABORTED. Fix the errors in YAML.")
        sys.exit(1)
    else:
        print("✅ Validation PASSED.")

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
            autoescape=False
        )
        template = env.get_template(os.path.basename(TEMPLATE_FILE))
    except jinja2.TemplateNotFound:
        print(f"Error: Template not found at {TEMPLATE_FILE}")
        sys.exit(1)

    print("Rendering cover letter...")
    rendered_tex = template.render(**escaped_data)
    
    if args.output:
        output_file = args.output
        output_dir = os.path.dirname(output_file)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
    else:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        filename = data.get("meta", {}).get("filename")
        if not filename:
            # Try to get role name
            # Check experience[0].role
            exp0 = data.get("experience", [{}])[0]
            role_name = exp0.get("role", "Generated")
            filename = f"Abhishek_Nagaraja_{role_name.replace(' ', '_')}_Cover_Letter"
        
        if "_Resume" in filename:
            filename = filename.replace("_Resume", "_Cover_Letter")
        elif "_Generated_Resume" in filename:
            filename = filename.replace("_Generated_Resume", "_Cover_Letter")
        elif ".tex" in filename:
             filename = filename.replace(".tex", "_Cover_Letter")
        elif "_Cover_Letter" not in filename:
            filename += "_Cover_Letter"
            
        if not filename.endswith(".tex"):
            filename += ".tex"
        output_file = os.path.join(OUTPUT_DIR, filename)
    
    print(f"Writing to {output_file}...")
    with open(output_file, 'w') as f:
        f.write(rendered_tex)
        
    print("✅ Cover Letter Generation COMPLETE.")

if __name__ == "__main__":
    main()
