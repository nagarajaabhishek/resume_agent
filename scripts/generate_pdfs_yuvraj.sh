#!/bin/bash

# Resume Generation Script using Tectonic for Yuvraj
# Usage: ./scripts/generate_pdfs_yuvraj.sh

cd "$(dirname "$0")/.."

# Check if tectonic is installed
if ! command -v tectonic &> /dev/null; then
    echo "Error: tectonic is not installed. Please run 'brew install tectonic' first."
    exit 1
fi

echo "Starting PDF generation for Yuvraj..."

# Find all .tex files in the Resume_Building/Yuvraj directory
find Resume_Building/Yuvraj -name "*.tex" | while read -r tex_file; do
    echo "Processing: $tex_file"
    
    # Remove existing PDF if it exists
    pdf_file="${tex_file%.tex}.pdf"
    if [ -f "$pdf_file" ]; then
        echo "Removing old PDF: $pdf_file"
        rm "$pdf_file"
    fi

    tex_dir=$(dirname "$tex_file")
    if tectonic --outdir "$tex_dir" "$tex_file"; then
        echo "✅ Successfully generated PDF for $tex_file"
    else
        echo "❌ Failed to generate PDF for $tex_file"
    fi
done

echo "PDF generation complete."
