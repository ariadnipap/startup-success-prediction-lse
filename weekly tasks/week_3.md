**Week 3 – Baseline Modeling & Evaluation**

This week we will train baseline machine learning models to establish performance benchmarks before tuning and optimization in Week 4.

We will:
1. Split the processed dataset into training and testing sets.
2. Train two baseline models:
   - Logistic Regression (linear baseline)
   - Random Forest (non-linear baseline)
3. Evaluate performance (accuracy, precision, recall, F1-score).
4. Generate plots and result files for discussion in the Friday meeting.

*Folder Structure Updates:*

Ensure these directories exist:

data/processed/        (already exists - final dataset from Week 2)
data/model_ready/      (New folder - store train/test splits)
docs/models/           (New folder - save model metrics and plots)

*Task Assignments:*

This week, we are rotating responsibilities to ensure everyone works directly with model development. The workflow will run: Cathy → Lan → Robert.

| Developer  | Task                                                                                                 | Skill Built                          | Output                                                                          |
| ---------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------- |
| **Cathy** | Perform train/test split once and push the split files. **Then train baseline Logistic Regression.** | Data preparation + linear modeling   | `logreg_classification_report.txt`, `logreg_cm.png`                             |
| **Lan**    | Train Random Forest baseline and generate feature importance plot                                    | Non-linear modeling + interpretation | `rf_classification_report.txt`, `rf_cm.png`, `rf_feature_importance.png`        |
| **Robert**  | Perform model performance comparison + create visualization comparing models                         | Evaluation + result communication    | `model_comparison.png` and a **short insights summary** (`model_comparison.md`) |

**Developer 1 – Train/Test Split + Logistic Regression (Cathy)**

Responsibilities:
- Load processed dataset
- Separate features (X) and target (y)
- Perform train/test split with stratification
- Train baseline Logistic Regression model
- Compute evaluation metrics (accuracy, precision, recall, F1-score)
- Generate confusion matrix heatmap

Outputs (saved in data/model_ready/ and docs/models/):

X_train.csv
X_test.csv
y_train.csv
y_test.csv
logreg_classification_report.txt
logreg_confusion_matrix.png

**Developer 2 – Random Forest & Feature Importance Lead (Lan)**

Responsibilities:
- Load the train/test data produced by Cathy
- Train Random Forest baseline model
- Compute evaluation metrics
- Generate confusion matrix heatmap
- Plot top 15 feature importances (horizontal bar plot)

Outputs (saved in docs/models/):

rf_classification_report.txt
rf_confusion_matrix.png
rf_feature_importance.png

**Developer 3 – Model Performance Comparison & Summary (Robert)**

Responsibilities:
- Load evaluation outputs from both models
- Create a clear visual comparison of performance (e.g., bar chart comparing F1-scores)
- Write a short insights summary explaining which model performs better and why

Outputs (saved in docs/models/):
model_comparison.png
model_comparison.md

Target variable:
status

Train/Test Split:
test_size = 0.2
random_state = 42
stratify = y

Evaluation Metrics:
accuracy, precision, recall, F1 score, confusion matrix

Feature importance (Random Forest):
Take the 15 highest-ranked features and plot them horizontally.

End-of-Week Deliverables:

- All scripts run without errors
- Train/test CSVs in data/model_ready/
- Model metrics and plots saved in docs/models/
- Work committed and pushed to GitHub

If anyone is blocked, message in the WhatsApp group and we resolve it together.
