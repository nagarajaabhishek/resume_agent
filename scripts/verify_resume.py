import os
import re
import sys

def verify_latex_file(file_path):
    print(f"Verifying {file_path}...")
    issues = []
    is_cover_letter = "Cover_Letter" in file_path
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines()

        # Bolding syntax check (LaTeX uses \textbf{}, not **)
        if "**" in content:
            issues.append("Found markdown bolding (**). Use \\textbf{} instead.")

        # Check for nested itemize in rSubsection
        # Logic: If we see \begin{rSubsection} and then \begin{itemize} before the next \end{rSubsection} or \item
        # This is a bit complex for simple regex, but we can check for \begin{itemize} generally.
        # Ideally, rSubsection content should use \item directly.
        # The pattern to avoid is \begin{rSubsection} ... \begin{itemize} ...
        
        # Simple check: Do we have \begin{itemize} inside the document body at all? 
        # The template uses \begin{list} inside environments. 
        # If the USER adds \begin{itemize}, it's usually wrong unless it's a specific sub-list (rare in this template).
        # Let's flag any availability of \begin{itemize} as a potential warning, 
        # but specifically if it's immediately following an rSubsection start or \item[]
        
        # Common Checks
        if "\\begin{itemize}" in content:
             # Check for uncommented itemize
             uncommented_itemize = len(re.findall(r"^[^%]*\\begin\{itemize\}", content, re.MULTILINE))
             if uncommented_itemize > 0:
                 issues.append(f"Found {uncommented_itemize} '\\begin{{itemize}}' environments. In 'rSubsection', use '\\item' directly to avoid double bullets/spacing issues.")

        if is_cover_letter:
            # Cover Letter Specific Checks
            # Cover Letter Specific Checks (from SKILL.md Section 14)
            if "\\today" in content:
                issues.append("Found '\\today' command. Cover letters MUST be timeless (no dates) per SKILL.md.")
            
            # Check for common placeholders
            placeholders = re.findall(r"\[.*?\]|\(.*?\)", content)
            for p in placeholders:
                # Ignore common LaTeX brackets if they aren't placeholders
                if any(word in p.lower() for word in ["company", "role", "manager", "hiring", "date", "address"]):
                    issues.append(f"Potential placeholder found: {p}. Ensure all letters use universal terms.")

            if "vspace{2.5em}" in content:
                issues.append("Signature spacing is too large (2.5em). Use 1.2em for better aesthetics.")
            
            if "\\setstretch{1.15}" not in content:
                issues.append("Missing premium line spacing (\\setstretch{1.15}).")
            
            # Check for consistent header (heuristic)
            if "Abhishek Nagaraja" not in content or "Arlington, Texas" not in content:
                 issues.append("Header seems inconsistent. Ensure it matches the Resume header exactly.")

        else:
            # Resume Specific Checks (Line Efficiency)
            # We want bullet points to be substantial.
            in_ignored_section = False
            
            for i, line in enumerate(lines):
                line = line.strip()
                
                # Detect section headers to toggle ignore flag
                if "\\begin{rSection}{Education" in line or "\\begin{rSection}{Skills" in line or "\\begin{rSection}{Certification" in line:
                    in_ignored_section = True
                elif "\\begin{rSection}{" in line:
                    in_ignored_section = False
                
                if (line.startswith("\\item ") or line.startswith("\\item[") or line.startswith("\\item{")) and not line.startswith("\\item[] \\vspace"):
                    # Check length of content
                    text_content = re.sub(r"\\item(\[.*?\])?", "", line).strip()
                    # Also ignore lines that are just \vspace (heuristic)
                    if "\\vspace" in text_content and len(text_content.replace("\\vspace", "").strip()) < 5:
                        continue
                    
                    # Ignore short lines in Skills/Education/Certs
                    if not in_ignored_section:
                        if len(text_content) < 80 and len(text_content) > 5: # Arbitrary threshold for "too short" but not empty
                            issues.append(f"Line {i+1}: Bullet point might be too short ({len(text_content)} chars). Aim for full lines.")
                
        # Check for explicit \\vspace hacks which might indicate manual spacing fixes
        if "\\vspace" in content:
             # Just a warning
             pass 

    except Exception as e:
        issues.append(f"Error reading file: {e}")

    if issues:
        print(f"❌ Issues found in {os.path.basename(file_path)}:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    else:
        print(f"✅ {os.path.basename(file_path)} looks good.")
        return True

def main():
    base_dir = "Resume_Building/Abhishek"
    has_error = False
    
    # Walk through directory
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".tex") and not file.startswith("single_file"):
                full_path = os.path.join(root, file)
                if not verify_latex_file(full_path):
                    has_error = True
    
    if has_error:
        print("\n⚠️  Verification completed with warnings.")
        # We don't exit 1 because these might be soft warnings, but user should see them.
    else:
        print("\n✅ Verification completed successfully.")

if __name__ == "__main__":
    main()
