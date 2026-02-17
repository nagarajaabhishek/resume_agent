# Cover Letter Rules

## 1. Non-Negotiable Formatting
1. **LaTeX Only**: Use `single_file_cover_letter_template.tex`.
2. **Timelessness**: **NEVER** include a date. No `\today`.
3. **Branding**: Must use the **EXACT SAME HEADER** layout, font (Charter), and contact info as the resume.
4. **Aesthetics**:
   - Font Size: **11pt**.
   - Line Spacing: `\setstretch{1.15}`.
   - Signature: "Sincerely," $\rightarrow$ `\vspace{1.2em}` $\rightarrow$ **Name in Bold**.

## 2. Narrative Strategy
1. **Hook:** State the specific value proposition for the role in the first sentence.
2. **Bridge:** Connect your past technical achievements to the company's future needs.
3. **Evidence:** Use ONE hero project that demonstrates both technical depth and leadership capability.
4. **Tone:** Professional yet proactive ("Builder Mindset"). Avoid "I am writing to apply..."; start with "As a Technical Leader specializing in...".

## 3. Constraints
1. **No Placeholders**: Never use `[Company Name]` or `[Job Title]` in the final file. Use general terms like "your team" or "this role" to maintain a timeless, ready-to-use quality.
2. **Word Count**: Keep between 300-350 words.
3. **Verification**: Must pass `verify_resume.py` (no placeholders, bolding syntax check).
