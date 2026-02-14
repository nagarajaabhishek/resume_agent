#!/bin/bash

# Check if a .tex file was provided
if [ -z "$1" ]; then
  echo "Usage: ./compile_resume.sh <path_to_tex_file>"
  exit 1
fi

TEX_FILE=$(basename "$1")
DIR_PATH=$(dirname "$(realpath "$1")")

echo "Compiling $TEX_FILE in $DIR_PATH using Docker..."

# Run pdflatex inside a Docker container
# Mounting the directory containing the .tex file to /data in the container
docker run --rm -i -v "$DIR_PATH":/data -w /data texlive/texlive pdflatex "$TEX_FILE"

# Check if the PDF was created
PDF_FILE="${TEX_FILE%.tex}.pdf"

if [ -f "$DIR_PATH/$PDF_FILE" ]; then
  echo "Success! PDF generated at: $DIR_PATH/$PDF_FILE"
else
  echo "Error: PDF generation failed."
  exit 1
fi
