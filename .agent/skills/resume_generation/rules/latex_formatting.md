# LaTeX Formatting Rules

## 1. Font & Typography (Charter Serif)
To maintain a consistent personal brand all documents use the Charter font.
1. **Implementation**: Ensure the preamble includes `\usepackage[T1]{fontenc}` followed by `\usepackage{charter}`.
2. **Compiler Compatibility (pdfLaTeX & Tectonic/XeTeX)**:
   - Always load `\usepackage[T1]{fontenc}` before `\usepackage{charter}` so both pdfLaTeX (Overleaf) and Tectonic/XeTeX properly bind the Bitstream Charter font metrics and bold/italic weights instead of falling back to Latin Modern Roman.
   - Include `\usepackage{newunicodechar}` with `\newunicodechar{—}{---}` and `\newunicodechar{–}{--}` to ensure native em-dash/en-dash rendering across engines.
   - Wrap `glyphtounicode` in `\usepackage{iftex}\ifpdftex ... \fi` to avoid undefined control sequence errors in XeTeX engines.
3. **Consistency**: Both the resume and cover letter must use the Charter font.
4. **Cover Letter Exception**: If specified, the classic LaTeX Serif (Computer Modern) can be used, but Charter is the default for branding unity.

## 2. Layout & Structure (ATS Optimization)
1. **No Columns or Tables**: Use a single-column layout only. Tables and columns are the #1 failure point for ATS parsers.
2. **No Graphics/Images**: Avoid icons, logos, and photos.
3. **Standard Section Order**:
   - Summary (No Header)
   - Education
   - Work Experience
   - Projects
   - Skills & Certifications

## 3. LaTeX Technical Constraints
1. **Bolding Syntax**: **ALWAYS** use `\textbf{text}`. **NEVER** use markdown `**text**`.
2. **Standard Headers**:
   - Title style: `\textbf{\Large Section Name}`.
   - Use `\hrule` after section titles.
3. **Environment Rules**:
   - No `\begin{itemize}` within `rSubsection`. Use `\item` directly for cleaner parsing.
   - Mismatched environments (e.g., `\end{document}` ended by `\end{list}`) are fatal errors.

## 4. Spacing (Uniform Branding)
1. **Name**: `\huge` font size.
2. **Post-Name Summary**: 17px or equivalent large font for the role title/credentials.
3. **Section Spacing**:
   - Space above the line: `\smallskip`.
   - Subsection skip: `\smallskip` after title/location line.
4. **Skills Section**: Use a single list or itemized categories. Bold the **Category Name**.
