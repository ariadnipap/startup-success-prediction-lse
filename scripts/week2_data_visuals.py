"""
WEEK 2 – EXPLORATORY DATA ANALYSIS (EDA)
Author: [Developer #3]
Task: Create a few visualizations or summary stats
to understand trends in the cleaned dataset.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

clean_path = Path("../data/cleaned/cleaned_startups.csv")
df = pd.read_csv(clean_path)

# --- TODO: Create at least 2–3 plots ---
# Examples:
# sns.countplot(x='status', data=df)
# sns.histplot(df['total_funding_usd'], bins=40)
# plt.show()

# --- TODO: Summarize insights ---
# (e.g. “Most successful startups are in the US and have higher funding.”)
