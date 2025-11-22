# Week 4 – Model Tuning & Interpretability (XGBoost + SHAP)

This week we move beyond the baseline models from Week 3 (Logistic Regression & Random Forest) and work on:

1. Building a more powerful model using XGBoost  
2. Tuning XGBoost’s hyperparameters to improve performance  
3. Interpreting the tuned model using SHAP  

By the end of this week, we should have a high-performing model AND a clear explanation of which features matter most for startup success.

# Recommended Learning Resources

To help understand the tools we’ll use:

### XGBoost
- Official introduction: https://xgboost.readthedocs.io/en/stable/tutorials/model.html  

### Hyperparameter Tuning
- Scikit-learn tuning documentation: https://scikit-learn.org/stable/modules/grid_search.html  

### SHAP
- Official SHAP documentation: https://shap.readthedocs.io/en/latest/  

# 👥 Task Assignments

Order this week: **Robert → Cathy → Lan**


# 1. Robert – Baseline XGBoost Model

### Goal
Build a basic XGBoost model (no tuning) to establish a reference.

### Tasks
- Load:
  - X_train.csv
  - X_test.csv
  - y_train.csv
  - y_test.csv
- Train a default XGBoost model, for example:
```
XGBClassifier(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    n_jobs=-1
)
```
- Evaluate on test set:
  - accuracy
  - precision
  - recall
  - F1 score
  - confusion matrix

### Outputs (save in docs/tuning_results/)
- xgboost_baseline_report.txt
- xgboost_baseline_cm.png

# 2. Cathy – Hyperparameter Tuning for XGBoost

### Goal
Improve Robert’s baseline XGBoost model using hyperparameter tuning.

### Script
`scripts/week4_xgboost_tuning.py`

### Tasks
- Load same train/test data
- Use RandomizedSearchCV with something like:
```
param_dist = {
    "n_estimators": [200, 300, 400, 500],
    "max_depth": [3, 5, 7, 9],
    "learning_rate": [0.01, 0.05, 0.1, 0.2],
    "subsample": [0.6, 0.8, 1.0],
    "colsample_bytree": [0.6, 0.8, 1.0],
    "min_child_weight": [1, 3, 5]
}
```
- And then proceed with something like:
```
RandomizedSearchCV(
    estimator,
    param_distributions=param_dist,
    n_iter=20,
    scoring="f1_weighted",
    cv=5,
    n_jobs=-1,
    verbose=1
)
```
- Fit the search
- Evaluate the best model on the test set
- Compare against Robert’s baseline

### Outputs (save in docs/tuning_results/)
- xgboost_best_params.json
- xgboost_tuned_report.txt
- xgboost_tuned_cm.png
- xgboost_cv_results.csv (optional but recommended)

------------------------------------------------------------

# 3. Lan – SHAP Feature Interpretability

### Goal
Explain why XGBoost makes its predictions using SHAP.

### Script
`scripts/week4_shap_analysis.py`

### Tasks
- Load Cathy’s tuned best model
- Load X_test
- Compute SHAP values:
```
explainer = shap.Explainer(best_model)
shap_values = explainer(X_test)
```
- Produce:
  - SHAP summary plot (global importance)
  - SHAP dependence plots (top 2–3 features)

### Outputs (save in docs/tuning_results/)
- shap_summary_plot.png
- shap_dependence_<feature>.png
- shap_insights.md (short explanation of findings)

# ✅ Deliverables (Due Friday 11:00 UK)

- Baseline XGBoost model (Robert)  
- Tuned XGBoost model + best hyperparameters (Cathy)  
- SHAP explainability visuals + insights (Lan)  
- All scripts complete and pushed to GitHub  

# End of Week Goal
A stronger, tuned model AND clear interpretation of feature importance and impact.
