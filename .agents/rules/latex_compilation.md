# LaTeX Formatting & Compilation Rule

## Mandatory Preamble for Charter Font
Whenever generating, editing, or compiling LaTeX resumes or cover letters in this repository, always ensure the preamble includes:

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

## Why this is required:
1. **Charter Font Binding**: `\usepackage[T1]{fontenc}` before `\usepackage{charter}` ensures that both Overleaf (pdfLaTeX) and local compilers (Tectonic/XeTeX) load the authentic Bitstream Charter Type 1 font family (`CharterBT-Roman`, `CharterBT-Bold`, `CharterBT-Italic`, `CharterBT-BoldItalic`) with full bolding rather than silently falling back to Latin Modern Roman.
2. **Native Dashes**: `newunicodechar` maps unicode em-dash `—` and en-dash `–` to native TeX ligature dashes in Charter.
3. **Engine-Safe Unicode Mapping**: `ifpdftex` prevents `\pdfgentounicode` undefined control sequence errors in XeTeX/Tectonic.
