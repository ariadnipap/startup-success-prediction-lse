"""
WEEK 2 – DATA CLEANING
Author: [Developer #1]
Task: Load the raw startup dataset, inspect it, handle missing values,
and export a cleaned version to data/cleaned/.
"""

import pandas as pd
from pathlib import Path

# --- Load dataset ---
raw_path = Path("../data/raw/startup_success.csv")
df = pd.read_csv(raw_path)

# --- Basic info ---
print(df.shape)
print(df.info())

# --- TODO: Handle missing values ---
# (e.g., fillna, dropna, replace)
# Example:
# df['total_funding_usd'] = df['total_funding_usd'].fillna(df['total_funding_usd'].median())

# --- TODO: Fix data types and duplicates ---
# df['founded_year'] = df['founded_year'].astype(int)
# df.drop_duplicates(inplace=True)

# --- Export cleaned data ---
output_path = Path("../data/cleaned/cleaned_startups.csv")
df.to_csv(output_path, index=False)
print(f"✅ Cleaned dataset saved to {output_path}")
