import json
import os

# Paths to input and output
INPUT_PAGE_JSON = "playwright_scraped/pages/scraped_pages.json"
INPUT_DOCS_JSON = "playwright_scraped/documents/scraped_documents.json"
OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Utility function to clean and flatten text
def clean_text(text):
    if not text:
        return ""
    return ' '.join(text.strip().split())

# Load and clean page content
with open(INPUT_PAGE_JSON, "r", encoding="utf-8") as f:
    page_content = json.load(f)

cleaned_pages = []
for entry in page_content:
    flat_text = clean_text(entry.get("extracted_text", ""))  # ✅ Corrected key
    if flat_text:
        cleaned_pages.append({
            "url": entry.get("url"),
            "text": flat_text
        })

# Load and clean document content
with open(INPUT_DOCS_JSON, "r", encoding="utf-8") as f:
    documents = json.load(f)

cleaned_docs = []
for entry in documents:
    flat_text = clean_text(entry.get("extracted_text", ""))  # ✅ Good
    if flat_text:
        cleaned_docs.append({
            "url": entry.get("url"),
            "file_name": entry.get("file_name"),
            "text": flat_text
        })

# Save as JSON
with open(os.path.join(OUTPUT_DIR, "cleaned_pages.json"), "w", encoding="utf-8") as f:
    json.dump(cleaned_pages, f, indent=2, ensure_ascii=False)

with open(os.path.join(OUTPUT_DIR, "cleaned_documents.json"), "w", encoding="utf-8") as f:
    json.dump(cleaned_docs, f, indent=2, ensure_ascii=False)

print("✅ Cleaning complete. Output saved in 'data' folder.")