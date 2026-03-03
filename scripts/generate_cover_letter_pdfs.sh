#!/bin/bash

# Cover Letter PDF Generation Script using Tectonic
# Usage: ./scripts/generate_cover_letter_pdfs.sh

cd "$(dirname "$0")/.."

# Check if tectonic is installed
if ! command -v tectonic &> /dev/null; then
    echo "Error: tectonic is not installed. Please run 'brew install tectonic' first."
    exit 1
fi

echo "Starting Cover Letter PDF generation..."

# Find all files containing "Cover_Letter" in the Resume_Building/Abhishek directory
find Resume_Building/Abhishek -name "*Cover_Letter*.tex" | while read -r tex_file; do
    echo "Processing: $tex_file"
    
    # Remove existing PDF if it exists
    pdf_file="${tex_file%.tex}.pdf"
    if [ -f "$pdf_file" ]; then
        echo "Removing old PDF: $pdf_file"
        rm "$pdf_file"
    fi

    # Run tectonic
    if tectonic "$tex_file"; then
        echo "✅ Successfully generated PDF for $tex_file"
    else
        echo "❌ Failed to generate PDF for $tex_file"
    fi
done

echo "Cover Letter PDF generation complete."
