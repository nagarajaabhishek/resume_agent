#!/usr/bin/env python3
"""
Comprehensive Resume Audit Script
Checks all resumes against SKILL.md rules
"""

import re
import os
from pathlib import Path

# Resume files to audit
RESUMES = {
    'BA': 'Resume_Building/Abhishek/Business_Analyst/Abhishek_Nagaraja_BA_Resume.tex',
    'SM': 'Resume_Building/Abhishek/Scrum_Master/Abhishek_Nagaraja_SM_Resume.tex',
    'PO': 'Resume_Building/Abhishek/Product_Owner/Abhishek_Nagaraja_PO_Resume.tex',
    'TPM': 'Resume_Building/Abhishek/Product/Abhishek_Nagaraja_TPM_Resume.tex',
    'Manager': 'Resume_Building/Abhishek/Manager/Abhishek_Nagaraja_Manager_Resume.tex',
    'GTM': 'Resume_Building/Abhishek/GTM/Abhishek_Nagaraja_GTM_Resume.tex',
}

def extract_bullets(content):
    """Extract all bullet points from LaTeX content"""
    # Match \item \textbf{Verb} ... pattern
    pattern = r'\\item\s+\\textbf\{([^}]+)\}([^\n]+(?:\n(?!\\item|\\end)[^\n]+)*)'
    matches = re.findall(pattern, content, re.MULTILINE)
    return [(verb, verb + text) for verb, text in matches]

def check_bullet_length(bullet_text):
    """Check if bullet is at least 2 lines (180-240 chars)"""
    # Remove LaTeX commands for accurate character count
    clean_text = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', bullet_text)
    clean_text = re.sub(r'\\[a-zA-Z]+', '', clean_text)
    clean_text = clean_text.replace('\\', '').strip()
    return len(clean_text)

def audit_resume(role, filepath):
    """Audit a single resume"""
    print(f"\n{'='*60}")
    print(f"AUDITING: {role} Resume")
    print(f"{'='*60}")
    
    if not os.path.exists(filepath):
        print(f"❌ File not found: {filepath}")
        return
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract bullets
    bullets = extract_bullets(content)
    print(f"\nTotal bullet points: {len(bullets)}")
    
    # Check action verb diversity
    verbs = [verb for verb, _ in bullets]
    unique_verbs = set(verbs)
    print(f"Unique action verbs: {len(unique_verbs)}")
    
    # Check for "Accomplished"
    accomplished_count = verbs.count('Accomplished')
    if accomplished_count > 0:
        print(f"⚠️  WARNING: {accomplished_count} instances of 'Accomplished'")
    else:
        print("✅ No 'Accomplished' repetition")
    
    # Check 2-line minimum
    print("\n--- 2-Line Minimum Check ---")
    short_bullets = []
    for i, (verb, bullet) in enumerate(bullets, 1):
        length = check_bullet_length(bullet)
        if length < 180:
            short_bullets.append((i, verb, length))
            print(f"⚠️  Bullet {i} ({verb}): {length} chars (< 180 minimum)")
    
    if not short_bullets:
        print("✅ All bullets meet 2-line minimum (180+ chars)")
    else:
        print(f"\n❌ {len(short_bullets)} bullets below minimum length")
    
    # Check for AI enhancement mentions
    ai_keywords = ['GenAI', 'GPT', 'Gemini', 'Claude', 'AI-powered', 'AI-driven', 'Agentic', 'LLM']
    ai_mentions = sum(1 for keyword in ai_keywords if keyword in content)
    print(f"\n--- AI Enhancement Check ---")
    if ai_mentions > 0:
        print(f"✅ Found {ai_mentions} AI-related mentions")
    else:
        print("⚠️  No explicit AI enhancement mentions")
    
    # Check Skills section
    print("\n--- Skills Triple-Threat Check ---")
    if 'Skills and Tools' in content or 'Skills' in content:
        print("✅ Skills section present")
        # Check for methodologies, tools, and concepts
        has_methodologies = any(word in content for word in ['Methodologies', 'Strategy', 'Agile', 'Scrum'])
        has_tools = any(word in content for word in ['Tools', 'Jira', 'Confluence', 'AWS'])
        has_concepts = any(word in content for word in ['Concepts', 'Architecture', 'DevOps'])
        
        if has_methodologies and has_tools:
            print("✅ Skills section includes Methodologies + Tools")
        else:
            print("⚠️  Skills section may be missing Methodologies or Tools")
    else:
        print("❌ No Skills section found")

def main():
    print("="*60)
    print("COMPREHENSIVE RESUME AUDIT - SKILL.md Compliance")
    print("="*60)
    
    for role, filepath in RESUMES.items():
        audit_resume(role, filepath)
    
    print(f"\n{'='*60}")
    print("AUDIT COMPLETE")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
