"""
WEEK 2 – FEATURE SELECTION & ENCODING
Author: [Developer #2]
Task: Choose which columns to keep and apply simple encodings
to prepare data for modeling.
"""

import pandas as pd
from pathlib import Path

clean_path = Path("../data/cleaned/cleaned_startups.csv")
df = pd.read_csv(clean_path)

# --- TODO: Drop irrelevant columns ---
# df = df.drop(columns=['company_name', 'permalink'])

# --- TODO: Encode categorical variables ---
# Example: pd.get_dummies or sklearn LabelEncoder
# df = pd.get_dummies(df, columns=['status'], drop_first=True)

# --- Export processed data ---
output_path = Path("../data/processed/feature_startups.csv")
df.to_csv(output_path, index=False)
print(f"✅ Feature dataset saved to {output_path}")
