# HR Data Analysis and Machine Learning Models

This repository contains an end‑to‑end HR analytics project focused on understanding factors related to employee attrition and building predictive machine learning models. The work was authored solely by **Owen Randolph** as part of **DSCI‑590: Applied Data Science**.

## Project Overview

The project uses IBM’s (fictional) HR Analytics Attrition dataset from Kaggle. It includes employee demographics, compensation, roles, and performance metrics.

- Dataset: [IBM HR Analytics – Attrition](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- Goals:
  - Perform data cleaning and preprocessing
  - Conduct exploratory data analysis (EDA) to uncover patterns in attrition
  - Build, tune, and evaluate ML models for attrition prediction
  - Summarize insights to inform HR recruitment and retention strategies

## Repository Contents

- `HR Data Analysis and ML Models.ipynb` – main Jupyter notebook with data prep, EDA, modeling, and evaluation
- `environment.yaml` – configuration file used by conda

## Methods

### Data Preparation
- Removed/merged redundant or low‑signal features (e.g., `EmployeeNumber`).
- Treated missing values and inconsistent categories (e.g., limited sales ratings).
- Encoded categorical variables and scaled numerics where appropriate.

### Exploratory Data Analysis (EDA)
- Univariate and bivariate distributions for key HR features.
- Correlation analysis against the attrition target.
- Visualizations of compensation, tenure, job role, and satisfaction vs. attrition.

### Modeling
- Baseline: Logistic Regression
- Tree‑based models: Decision Tree, Random Forest, Gradient Boosting
- Evaluation metrics: Accuracy, Precision, Recall, F1, ROC–AUC
- Model comparison and feature importance analysis

## Key Findings (Summary)
- Compensation, tenure, and job satisfaction are strong signals for attrition.
- Tree‑based models (Random Forest / Gradient Boosting) outperformed the logistic baseline.
- Top drivers included monthly income, years at company, and satisfaction‑related features.
## Author

**Owen Randolph**  
Sole author and maintainer
