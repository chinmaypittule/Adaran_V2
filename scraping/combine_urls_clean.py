import os
import pandas as pd

# Folder containing individual Excel files
input_folder = "sitemap_excels"

# Collect all DataFrames
all_urls = []

for file in os.listdir(input_folder):
    if file.endswith(".xlsx"):
        path = os.path.join(input_folder, file)
        try:
            df = pd.read_excel(path, usecols=["URL"])
            all_urls.append(df)
            print(f"✅ Loaded {len(df)} URLs from {file}")
        except Exception as e:
            print(f"❌ Error reading {file}: {e}")

# Combine all data
combined_df = pd.concat(all_urls, ignore_index=True)

# Show count before cleaning
before = len(combined_df)

# Normalize URLs
combined_df["URL"] = combined_df["URL"].astype(str)
combined_df["URL"] = combined_df["URL"].str.rstrip("/")        # Remove trailing slash
combined_df["URL"] = combined_df["URL"].str.strip()            # Remove leading/trailing spaces
# combined_df["URL"] = combined_df["URL"].str.lower()          # Optional: lowercase URLs

# Drop duplicates
combined_df.drop_duplicates(subset=["URL"], inplace=True)
after = len(combined_df)

# Save to Excel
output_file = "all_jsom_urls_combined.xlsx"
combined_df.to_excel(output_file, index=False)

print("\n✅ Combined sitemap URLs saved to:", output_file)
print(f"🔢 URLs before cleaning: {before}")
print(f"🔁 Unique URLs after cleaning: {after}")