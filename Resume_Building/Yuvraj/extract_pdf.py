
import pypdf
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        reader = pypdf.PdfReader(pdf_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

base_path = "/Users/abhisheknagaraja/Documents/Resume_Agent/Resume_Building/Yuvraj"
pdf_files = ["Profile.pdf", "Yuvraj_K.pdf", "resume.pdf"]
output_file = f"{base_path}/extracted_context.txt"

with open(output_file, "w") as f:
    for pdf_file in pdf_files:
        path = os.path.join(base_path, pdf_file)
        print(f"Extracting from: {path}")
        content = extract_text_from_pdf(path)
        f.write(f"--- START OF {pdf_file} ---\n")
        f.write(content)
        f.write(f"--- END OF {pdf_file} ---\n\n")

print(f"Extraction complete. Text saved to {output_file}")
