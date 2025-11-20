# Week 5 – Final Evaluation & Visualization

We are now done with modeling and tuning.  
This week focuses only on producing polished visualizations, comparisons, and clear interpretability insights.

## Goals for Week 5
- Bring together results from all models
- Create final polished visualizations
- Summarize model performance clearly
- Prepare interpretability insights (SHAP)
- Finalize confusion matrices for all models
- Organize outputs for final presentation and documentation

Models included:
- Logistic Regression
- Random Forest
- XGBoost

# 1. Robert – Final Model Comparison Plots

### Tasks:
- Load the metrics from:
  - Logistic Regression  
  - Random Forest  
  - XGBoost
- Create:
  - A bar chart comparing Accuracy, Precision, Recall, F1
  - A clean table of all metrics (CSV)
- Use consistent colors and readable labels

### Outputs (save in `docs/final_evaluation/`):
- `model_comparison_plot.png`
- `comparison_metrics.csv`

# 2. Lan – SHAP Interpretation Summary

### Tasks:
- Use the SHAP values and plots generated last week
- Save and organize:
  - SHAP summary plot (global feature importance)
  - SHAP dependence plots for the top 2–3 features
- Write a short interpretability summary describing:
  - Which features are most important
  - How SHAP explains the model’s predictions
  - Whether the explanations match intuition about startups

### Outputs (save in `docs/final_evaluation/`):
- `shap_summary_plot.png`
- `shap_dependence_<feature>.png`
- `shap_interpretation.md`

# 3. Cathy – Confusion Matrix Gallery + Visual Cleanup

### Tasks:
- Generate confusion matrices for:
  - Logistic Regression
  - Random Forest
  - XGBoost Baseline
  - XGBoost Tuned
- Ensure all confusion matrices have:
  - Same colormap
  - Same style
  - Same axis labels and fonts
  - Same layout and resolution
- Organize all final visuals:
  - SHAP plots
  - Feature importance plots
  - Confusion matrices
- Clean up folder structure and remove duplicates

### Outputs (save in `docs/final_visuals/confusion_matrices/`):
- `lr_confusion_matrix.png`
- `rf_confusion_matrix.png`
- `xgb_cm.png`

# Folder Structure for Week 5

```
docs/
    final_evaluation/
        model_comparison_plot.png
        comparison_metrics.csv
        shap_interpretation.md

    final_visuals/
        confusion_matrices/
            lr_confusion_matrix.png
            rf_confusion_matrix.png
            xgb_cm.png

        shap_plots/
        feature_importances/
```

# End-of-Week Deliverables

- Final model comparison plot  
- Comparison metrics table  
- SHAP summary visualizations  
- SHAP interpretation summary  
- Confusion matrix gallery  
- Clean, organized visuals folders  
- Prepared visuals for Week 6 documentation and final presentation

