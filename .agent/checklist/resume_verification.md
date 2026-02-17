
# Resume Verification Checklist

When generating a resume, ALWAYS verify the following:

1. **URLs**: Check that projects and education entries with URLs in the YAML are rendered with `\href{url}{name}` in the LaTeX.
2. **Formatting**: Ensure headers are formatted correctly (e.g., one-line for Work Experience if requested).
3. **Content**: Verify new skills or sections (like "Prototyping & Vibe Coding") are present.

## Automated Check
Run this command to verify URLs are present:
```bash
grep "\\href" Resume_Building/Generated/Generated_Resume.tex
```
