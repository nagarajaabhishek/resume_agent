import re
import os

def check_line_lengths(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith("_Resume.tex"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r') as f:
                    content = f.read()
                
                print(f"\n--- Auditing: {file} ---")
                # Look for items in rSubsection or itemize
                items = re.findall(r'\\item\s+(.*)', content)
                for item in items:
                    clean_item = re.sub(r'\\textbf\{|\}', '', item)
                    length = len(clean_item)
                    # 115-120 is 1 line. 230-240 is 2 lines.
                    if 125 < length < 180:
                        print(f"Potential Orphan (2nd line <50%): {length} chars: {clean_item[:50]}...")
                    elif length < 80:
                        print(f"Too short (line <70%): {length} chars: {clean_item[:50]}...")
                    else:
                        pass # print(f"Good length: {length} chars")

if __name__ == "__main__":
    check_line_lengths("/Users/abhisheknagaraja/Documents/Resume_Agent/Resume_Building/Abhishek/")
