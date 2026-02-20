import sys
from pypdf import PdfReader

try:
    reader = PdfReader("/Users/abhisheknagaraja/Documents/Resume_Agent/Resume_Building/Yuvraj/Data_Analyst/Data Analyst.pdf")
    print(f"Number of pages: {len(reader.pages)}")
    text_content = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        print(f"--- Page {i+1} ---")
        if text:
            print(text[:500] + "..." if len(text) > 500 else text) 
            text_content.append(text)
        else:
            print("[No text extracted from this page]")
    
    if not any(text_content):
        print("\nTOTAL FAILURE: No text extracted from any page.")
except Exception as e:
    print(f"Error: {e}")
