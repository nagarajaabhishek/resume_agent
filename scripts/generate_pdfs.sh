#!/bin/bash

# Resume Generation Script using Tectonic
# Usage: ./generate_pdfs.sh

cd "$(dirname "$0")/.."

# Check if tectonic is installed
if ! command -v tectonic &> /dev/null; then
    echo "Error: tectonic is not installed. Please run 'brew install tectonic' first."
    exit 1
fi

echo "Starting Verification..."
python3 scripts/verify_resume.py

echo "Starting PDF generation..."

# Find all .tex files in the Resume_Building/Abhishek directory
# Excluding the template files if any (though template is usually single_file_resume_template.tex in resources)
find Resume_Building/Abhishek -name "*.tex" | while read -r tex_file; do
    echo "Processing: $tex_file"
    
    # Remove existing PDF if it exists
    pdf_file="${tex_file%.tex}.pdf"
    if [ -f "$pdf_file" ]; then
        echo "Removing old PDF: $pdf_file"
        rm "$pdf_file"
    fi

    # Run tectonic
    # We use --keep-intermediates just in case debug is needed, but default is fine.
    # tectonic handles multiple runs automatically.
    if tectonic "$tex_file"; then
        echo "✅ Successfully generated PDF for $tex_file"
    else
        echo "❌ Failed to generate PDF for $tex_file"
    fi
done

echo "PDF generation complete."
