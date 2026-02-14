import sys
import os
import re
from collections import Counter
import math

try:
    from pdfminer.high_level import extract_text
except ImportError:
    print("Error: pdfminer.six is not installed. Please install it using: pip install pdfminer.six")
    sys.exit(1)

def clean_text(text):
    """
    Cleans text by removing special characters, lowercasing, and removing extra whitespace.
    """
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def get_cosine_similarity(text1, text2):
    """
    Calculates cosine similarity between two texts.
    """
    vec1 = Counter(text1.split())
    vec2 = Counter(text2.split())
    
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def calculate_ats_score(resume_path, jd_path):
    """
    Calculates an ATS score based on keyword matching and cosine similarity.
    """
    print(f"Analyzing Resume: {resume_path}")
    print(f"Against JD: {jd_path}")

    # Extract text from PDF
    try:
        resume_text = extract_text(resume_path)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return

    # Read JD text
    try:
        with open(jd_path, 'r', encoding='utf-8') as f:
            jd_text = f.read()
    except Exception as e:
        print(f"Error reading JD file: {e}")
        return

    # Clean texts
    clean_resume = clean_text(resume_text)
    clean_jd = clean_text(jd_text)

    # 1. Keyword Matching (Simple)
    # Extract potential keywords from JD (words > 3 chars, appearing more than once could be better but keeping it simple)
    # For a better approach, we'd use NLTK/Spacy to exact nouns/entities.
    # Here we will just look for unique words in JD and see coverage in Resume.
    
    jd_words = set(clean_jd.split())
    # Filter out common stop words (very basic list)
    stop_words = {'the', 'and', 'to', 'of', 'a', 'in', 'is', 'that', 'for', 'it', 'as', 'was', 'with', 'on', 'are', 'be', 'this', 'an', 'at', 'by', 'from', 'or', 'which', 'but', 'not', 'what', 'all', 'were', 'we', 'when', 'your', 'can', 'said', 'there', 'use', 'date', 'each', 'if', 'will', 'up', 'other', 'about', 'out', 'many', 'then', 'them', 'these', 'so', 'some', 'her', 'would', 'make', 'like', 'him', 'into', 'time', 'has', 'look', 'two', 'more', 'write', 'go', 'see', 'number', 'no', 'way', 'could', 'people', 'my', 'than', 'first', 'water', 'been', 'call', 'who', 'oil', 'its', 'now', 'find'}
    
    relevant_keywords = {word for word in jd_words if word not in stop_words and len(word) > 2}
    
    resume_words = set(clean_resume.split())
    
    matched_keywords = relevant_keywords.intersection(resume_words)
    missing_keywords = relevant_keywords - resume_words
    
    keyword_match_score = (len(matched_keywords) / len(relevant_keywords)) * 100 if relevant_keywords else 0

    # 2. Cosine Similarity (Contextual Match)
    similarity_score = get_cosine_similarity(clean_resume, clean_jd) * 100

    # Final Weighted Score
    # Weighing Keyword Match higher as ATS often filters by keywords first
    final_score = (keyword_match_score * 0.6) + (similarity_score * 0.4)

    print("\n" + "="*30)
    print(f"ATS MATCH SCORE: {final_score:.2f}%")
    print("="*30)
    print(f"Keyword Match Rate: {keyword_match_score:.2f}%")
    print(f"Cosine Similarity: {similarity_score:.2f}%")
    print("-" * 30)
    print(f"Missing Keywords (Top 10 sample): {list(missing_keywords)[:10]}")
    print("="*30)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ats_score.py <path_to_resume_pdf> <path_to_jd_txt>")
        sys.exit(1)
    
    resume_pdf = sys.argv[1]
    jd_txt = sys.argv[2]
    
    calculate_ats_score(resume_pdf, jd_txt)
