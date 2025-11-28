# Predicting Startup Success Using Machine Learning
**LSE Data Science Society Project (Autumn 2025)**  
**Project Lead:** Ariadni Papanikolaou  

---

## Overview
This project aims to build a predictive machine learning model that estimates a startup’s likelihood of success using publicly available business and funding data from Kaggle.  
By analyzing features such as founding year, total funding, location, and industry, the goal is to identify the most influential factors driving startup outcomes (success, acquisition, or closure).

**Dataset:** [Startup Success Prediction Dataset](https://www.kaggle.com/datasets/manishkc06/startup-success-prediction)  
**Source:** Kaggle (CC0 Public Domain License)

---

## Objectives
- Clean and preprocess a real-world dataset of 48,000+ startups  
- Engineer and select meaningful predictive features  
- Build and evaluate classification models (Logistic Regression, Random Forest, XGBoost)  
- Analyze feature importance and model interpretability (using SHAP)  
- Visualize insights through exploratory data analysis and results dashboards  

---

## Repository Structure
```
startup-success-prediction-lse/
│
├── data/
│   ├── raw/              # Original dataset from Kaggle
│   ├── cleaned/          # Cleaned dataset (Week 2)
│   └── processed/        # Feature-engineered dataset
│
├── scripts/
│   ├── week2_cleaning.py     # Data cleaning logic (missing values, types, duplicates)
│   ├── week2_features.py     # Feature selection & encoding
│   └── week2_visuals.py      # Exploratory data analysis & visualizations
│
├── weekly_tasks/
│   └── week2_tasks.md        # Detailed task plan for Week 2
│
├── docs/                     # Literature review, meeting notes, plots, reports
│
├── requirements.txt          # Python dependencies
└── README.md                 # Project overview, workflow, and structure

```

---

## Weekly Timeline

| Week | Focus | Main Deliverables |
|------|--------|-------------------|
| **1** | Literature Review & Dataset Exploration | Review of startup analytics + dataset inspection |
| **2** | Data Cleaning, Feature Selection, EDA | Cleaned data, engineered features, visual insights |
| **3** | Baseline Modeling | Logistic Regression, Random Forest |
| **4** | Model Tuning & Interpretability | XGBoost optimization, SHAP feature analysis |
| **5** | Evaluation & Visualization | Metrics, plots, comparison of models |
| **6** | Final Report & Presentation | Summary, visual dashboard (optional Streamlit) |

---

## Tech Stack
- **Python** (pandas, NumPy, scikit-learn, XGBoost, matplotlib, seaborn, SHAP)  
- **GitHub** for version control and documentation  
- **Streamlit (optional)** for final dashboard visualization  

---

## Team Guidelines
- Work on your assigned code first before editing others’.  
- Always add clear commit messages.   
- Weekly syncs will be used to review progress and merge work.

---

## Notes
This repository will evolve each week as we build, evaluate, and document our progress.  
All contributions, analyses, and visualizations will be integrated into the final project report.

---

**LSE Data Science Society – Predicting Startup Success Project**  
© 2025 | Ariadni Papanikolaou and Project Team
