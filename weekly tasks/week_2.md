# 📅 Week 2 – Data Cleaning, Feature Engineering & EDA
**Timeline:** Monday → Friday  
**Meeting:** Friday 14:00 – 15:00 (Teams)  
**Goal:** Transform the raw startup dataset into a clean, structured, and partially explored dataset ready for baseline modeling in Week 3.

---

## 🎯 Overall Objectives
1. Understand the dataset: variables, data types, and inconsistencies.  
2. Produce a **cleaned dataset** (no missing or invalid values).  
3. Generate a **feature-engineered dataset** suitable for ML models.  
4. Produce at least 2–3 **plots** or summary visuals showing insights.  
5. Document all findings and decisions for review in Friday’s meeting.

---

## 👥 Task Breakdown

| Member | File | Responsibilities | Deliverables |
|---------|------|------------------|---------------|
| **Developer 1 – [Name]** | `scripts/week2_cleaning.py` | - Load and inspect raw CSV<br>- Identify & handle missing values<br>- Fix data types, duplicates, and categorical inconsistencies<br>- Export cleaned data to `/data/cleaned/cleaned_startups.csv` | • Cleaned CSV<br>• Short list of cleaning steps performed |
| **Developer 2 – [Name]** | `scripts/week2_features.py` | - Select relevant columns<br>- Encode categorical variables (LabelEncoder / One-Hot)<br>- Normalize or scale if needed<br>- Export processed data to `/data/processed/feature_startups.csv` | • Processed CSV<br>• Notes on chosen features & encoding approach |
| **Developer 3 – [Name]** | `scripts/week2_visuals.py` | - Produce at least 3 visualizations (status distribution, funding histograms, correlations, etc.)<br>- Write short markdown summary of insights<br>- Save plots to `/docs/` | • `.png` plots<br>• 1-paragraph EDA summary |

---

## 🧾 Submission & Review
- Commit and push updates to GitHub by **Friday 11:00 AM**.  
- All output files (`.csv` and `.png`) should be saved in the correct folders.  
- During the meeting, we’ll discuss cleaning/feature choices and prepare for Week 3 (baseline modeling).

---

## 🧠 Notes
- Keep commits descriptive: e.g. `git commit -m "Filled missing values and standardized country codes"`.  
- If something breaks, push your partial progress anyway so we can debug together.  
- Optional but encouraged: include markdown comments explaining reasoning inside your scripts.

---
