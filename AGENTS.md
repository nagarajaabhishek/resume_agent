# Workspace Instructions & Rules

## LaTeX Typography & Compiler Compatibility
When generating, updating, or compiling resumes or LaTeX documents:
- **Font**: Must use **Charter** (`\usepackage{charter}`) with full **Bitstream Charter** bold/italic support.
- **Preamble Standard**:
  ```latex
  \usepackage[T1]{fontenc}
  \usepackage{charter}
  \usepackage{newunicodechar}
  \newunicodechar{—}{---}
  \newunicodechar{–}{--}
  \usepackage{iftex}
  \ifpdftex
    \input{glyphtounicode}
    \pdfgentounicode=1
  \fi
  ```
- **Local Compiler**: Use `tectonic --outdir <dir> <file>.tex`.
- **Target Styling**: Identical to Overleaf pdfLaTeX output with rich bolding (`\textbf{}`) and Charter typography.
