import requests
import sys
import re

def download_wikitext():
    # Correct URL for WikiText-2 (using 'main' branch)
    url = "https://raw.githubusercontent.com"
    filename = "wikitext_clean.txt"
    
    print(f"Attempting download from: {url}")
    
    try:
        # Get data with a timeout and header info
        response = requests.get(url, allow_redirects=True, timeout=10)
        
        # Check if the URL is actually valid (avoid saving 404 error pages)
        if response.status_code != 200:
            print(f"Error: Server returned status code {response.status_code}")
            sys.exit(1)

        text = response.text
        
        if not text or len(text) < 100:
            print("Error: Downloaded content is empty or too short.")
            sys.exit(1)

        # CLEANING:
        # 1. Remove Wikipedia headers (e.g., " = = = Robert Boulter = = = ")
        text = re.sub(r'(?m)^=+\s?.*?\s?=+$', '', text)
        # 2. Collapse multiple newlines to single paragraph breaks
        text = re.sub(r'\n{3,}', '\n\n', text).strip()

        # Write to file
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
            
        size_kb = len(text) / 1024
        print(f"✅ Success! Saved '{filename}'")
        print(f"📊 File Size: {size_kb:.2f} KB")
        
    except Exception as e:
        print(f"Download failed: {e}")

if __name__ == "__main__":
    download_wikitext()

