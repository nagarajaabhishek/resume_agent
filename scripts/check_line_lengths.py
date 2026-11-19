import os
import re
import sys


def check_line_lengths(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith("_Resume.tex"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    content = f.read()

                print(f"\n--- Auditing: {filepath} ---")
                items = re.findall(r'\\item\s+(.*)', content)
                for item in items:
                    clean_item = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', item)
                    length = len(clean_item)
                    # Standard 2-line target is 215-245 chars (~115-120 chars/line)
                    if 125 < length < 215:
                        print(f"Short / Potential Orphan ({length} chars < 215): {clean_item[:60]}...")
                    elif length > 245:
                        print(f"Over 2-line target ({length} chars > 245): {clean_item[:60]}...")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "Resume_Building"
    check_line_lengths(target)
