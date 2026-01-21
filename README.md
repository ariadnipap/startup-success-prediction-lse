# Predicting Startup Success Using Machine Learning
**LSE Data Science Society Project (Autumn 2025)**  
**Project Lead:** Ariadni Papanikolaou  

---

## Overview
This project develops an end-to-end machine learning pipeline to predict startup success using publicly available business and funding data from Kaggle.  
Startup success is defined as a positive exit (acquisition or IPO), while failure corresponds to company closure.

By analysing features such as funding history, milestone progression, company age, and industry indicators, the project aims to both:
1. **Accurately predict startup outcomes**, and  
2. **Provide interpretable insights** into the key drivers of success.

The emphasis is not only on predictive performance, but also on explainability and practical relevance for decision-making contexts such as venture capital and startup evaluation.

**Dataset:** Startup Success Prediction Dataset (Kaggle, CC0 License)

---

## Project Objectives
- Clean and preprocess a real-world startup dataset  
- Engineer and select meaningful predictive features  
- Train and evaluate multiple classification models  
- Compare model performance using standard evaluation metrics  
- Interpret model behaviour using SHAP explainability techniques  
- Communicate results through clear visualisations and reporting  

---

## Methodology Summary

### Data Preparation
- Removed identifiers and non-informative fields  
- Handled missing values and inconsistencies  
- Encoded categorical variables into numeric representations  
- Constructed a fully numeric, modeling-ready dataset  

### Modeling
The following models were trained and evaluated:
- **Logistic Regression** (linear baseline)
- **Random Forest** (non-linear baseline)
- **XGBoost** (gradient boosting, baseline and tuned)

Models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrices

### Interpretability
To ensure transparency, SHAP (SHapley Additive exPlanations) was applied to the final XGBoost model to:
- Identify globally important features
- Analyse how individual features influence predictions
- Validate whether learned patterns align with domain intuition

---

## Key Findings
- Tree-based models (Random Forest and XGBoost) significantly outperformed Logistic Regression, indicating strong non-linear relationships in the data.
- XGBoost achieved the best overall balance across evaluation metrics.
- Milestone progression, funding history, and company longevity emerged as the strongest predictors of success.
- SHAP analysis confirmed intuitive patterns, such as diminishing returns on funding and the importance of sustained progress over time.

---

## Project Timeline

| Week | Focus |
|------|------|
| 1 | Literature review & dataset exploration |
| 2 | Data cleaning, feature selection, exploratory analysis |
| 3 | Baseline modeling (Logistic Regression, Random Forest) |
| 4 | Advanced modeling & interpretability (XGBoost, SHAP) |
| 5 | Evaluation, comparison & visualization |
| 6 | Final report & presentation |

---

## Tech Stack
- **Python**: pandas, NumPy, scikit-learn, XGBoost  
- **Visualization**: matplotlib, seaborn  
- **Interpretability**: SHAP  
- **Version Control & Collaboration**: GitHub  

---

## Team & Collaboration
This project was completed collaboratively as part of the LSE Data Science Society.  
Work was organised through weekly task plans, version-controlled scripts, and regular sync meetings to review progress and align on next steps.

---

## Final Outputs
- Fully documented machine learning pipeline  
- Comparative evaluation of multiple models  
- Interpretable insights into startup success drivers  
- Final written report and presentation materials  

---

**LSE Data Science Society – Predicting Startup Success Project**  
© 2025 | Ariadni Papanikolaou, Robert Chen, Lan Nguy, Cathy Yang
