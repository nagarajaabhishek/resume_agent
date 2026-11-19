#!/bin/bash

# Resume Generation Script using Tectonic
# Usage: ./scripts/generate_pdfs.sh [PersonName]
# Example: ./scripts/generate_pdfs.sh Abhishek

cd "$(dirname "$0")/.." || exit 1

if ! command -v tectonic &> /dev/null; then
    echo "Error: tectonic is not installed. Please run 'brew install tectonic' first."
    exit 1
fi

TARGET_DIR="Resume_Building"
if [ -n "$1" ]; then
    TARGET_DIR="Resume_Building/$1"
fi

if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: Target directory '$TARGET_DIR' not found."
    exit 1
fi

echo "Starting PDF generation in $TARGET_DIR..."

find "$TARGET_DIR" -name "*.tex" | while read -r tex_file; do
    echo "Processing: $tex_file"

    pdf_file="${tex_file%.tex}.pdf"
    if [ -f "$pdf_file" ]; then
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
