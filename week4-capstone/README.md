# Week 4 Capstone — Predicting Internship Selection Outcomes

A Machine Learning project that explores applicant data and predicts internship selection outcomes using classification models.

## 1. Project Objective

The objective of this project is to explore factors associated with internship selection outcomes at NextGenLearners and build machine learning models to predict whether an applicant is likely to be selected or not.

## 2. Dataset Description

The project uses the cleaned applicant dataset from Week 1, containing 75 records and 7 original columns.

Four additional features were generated to support the machine learning exercise:

- `num_skills_listed`: Number of skills listed by the applicant.
- `has_portfolio`: Whether the applicant has a portfolio.
- `prior_hackathon_participation`: Whether the applicant previously participated in a hackathon.
- `statement_quality_score`: A simulated score representing the quality of the applicant's written statement.

**Important:** These four additional features are simulated data, not actual historical applicant information.

After excluding applicants with pending decisions (Under Review), the final modeling dataset contained 43 applicants:
- 25 Rejected.
- 18 Selected.

## 3. Methodology

The project followed these main steps:

1. **Data Loading:** Loaded the cleaned applicant dataset.
2. **Feature Engineering:** Generated four simulated features.
3. **Data Preparation:** Converted Yes/No values into binary values, created the target variable, and applied One-Hot Encoding to applicant domains.
4. **Train/Test Split:** Divided the dataset into 80% training and 20% testing data.
5. **Model Training:** Trained Logistic Regression and Decision Tree models, with KNN as an additional experiment.
6. **Model Evaluation:** Evaluated performance using Accuracy, Precision, Recall, and Confusion Matrices.
7. **Feature Importance:** Analyzed the features used by the Decision Tree model.

## 4. Key Results

The following results were obtained on the test dataset (9 applicants):

| Model | Accuracy |
|---|---:|
| Logistic Regression | 33.33% |
| Decision Tree | 55.56% |
| KNN | 66.67% |

**Additional Evaluation:**

- Decision Tree achieved 60% Precision and 60% Recall.
- KNN achieved 100% Precision and 40% Recall.
- Logistic Regression achieved 0% Precision and 0% Recall.

KNN achieved the highest test accuracy among the three models in this experiment.

**Feature Importance:**

The Decision Tree relied most heavily on:
1. Statement Quality Score (51.66%).
2. Number of Skills Listed (27.18%).
3. Prior Hackathon Participation (12.24%).
4. Portfolio Availability (8.93%).

The encoded domain features had zero importance in this trained tree.

## 5. Limitations

- The dataset is small, containing only 43 applicants with confirmed outcomes.
- Four features were simulated rather than collected from real applicant records.
- The test set contains only 9 applicants, making evaluation results sensitive to individual predictions.
- The Decision Tree showed a noticeable gap between training and testing performance, suggesting possible overfitting.

Therefore, the results are experimental and should not be considered evidence of actual internship selection criteria.

The models should only support human reviewers and must never replace human judgment.

## 6. How to Run the Project

1. Clone or download this repository.
2. Open `Week4_Capstone_Mohraeil_Maged.ipynb` in Jupyter Notebook or Google Colab.
3. Make sure `applicants_cleaned.csv` is available in the same working directory as the notebook.
4. Install the required libraries if they are not already installed:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

5. Run all notebook cells from top to bottom.

## 7. Walkthrough Video

[Add your project walkthrough video link here]