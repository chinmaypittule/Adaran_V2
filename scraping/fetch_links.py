import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin, urlparse
import os

# List of sitemap URLs
sitemaps = [
    "https://osim.utdallas.edu/sitemap/",
]

# Create an output folder
output_dir = "sitemap_excels"
os.makedirs(output_dir, exist_ok=True)

def extract_links(sitemap_url):
    links = []
    try:
        res = requests.get(sitemap_url)
        soup = BeautifulSoup(res.content, 'html.parser')
        for a in soup.find_all('a', href=True):
            full_url = urljoin(sitemap_url, a['href'])
            links.append(full_url)
    except Exception as e:
        print(f"Error processing {sitemap_url}: {e}")
    return links

# Loop through each sitemap and save to its own Excel file
for sitemap in sitemaps:
    domain_name = urlparse(sitemap).hostname.split('.')[0]
    links = extract_links(sitemap)
    print(f"Found {len(links)} links in {domain_name}")

    df = pd.DataFrame(sorted(set(links)), columns=["URL"])
    output_file = os.path.join(output_dir, f"{domain_name}_sitemap_urls.xlsx")
    df.to_excel(output_file, index=False)
    print(f"Saved to {output_file}")