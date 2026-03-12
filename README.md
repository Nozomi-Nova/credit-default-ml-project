# Credit Default ML Project

## Overview

This project is for **DS4420 – Machine Learning and Data Mining 2 (Spring 2026)** at Northeastern University. We study **credit‑card default prediction** using real data and compare two closely related but conceptually different modeling approaches:

1. A **manual frequentist logistic regression** implemented from scratch in Python.  
2. A **Bayesian logistic regression** implemented in R.

Instead of focusing only on predictive accuracy, we emphasize:

- **Calibration** – how well predicted default probabilities match observed default rates.  
- **Uncertainty quantification** – how confident the models are in their predictions, especially near decision thresholds.

The goal is to understand how trustworthy the predicted probabilities of default (PDs) are, and whether Bayesian inference offers a more honest treatment of uncertainty than a conventional logistic model.

## Data

### Primary dataset: Taiwan credit card default

- Source: UCI Machine Learning Repository – *Default of Credit Card Clients*.  
- Observations: 30,000 cardholders.  
- Features (23 predictors):  
  - Credit limit, age, sex, education, marital status.  
  - Six months of payment status (PAY_0, PAY_2, …, PAY_6).  
  - Six months of bill amounts (BILL_AMT1–6).  
  - Six months of payment amounts (PAY_AMT1–6).  
- Target: `default` (binary, 1 = default next month, 0 = no default).  
- Default rate: approx **22%**.

Data are loaded directly from the UCI URL inside the notebooks; no raw data files are stored in this repo.

### Optional secondary dataset: German credit

We may later include the classic UCI **German credit** dataset as a secondary robustness check. For Phase I, all analyses focus on the Taiwan dataset.

## Methods

The project centers on **two primary methods**:

1. **Manual logistic regression (Python)**  
   - Implemented from scratch using NumPy and gradient descent.  
   - Serves as our main **frequentist classifier**.  
   - Trained on standardized features with the same train–test split as all other models.  
   - Evaluated on AUC, precision/recall/F1, and especially on **calibration** (reliability curves, Brier score).

2. **Bayesian logistic regression (R)**  
   - Supervised Bayesian model for the same binary default outcome.  
   - Coefficients have prior distributions; inference is done via Bayesian methods (e.g., MCMC or variational inference).  
   - Produces **posterior distributions** for coefficients and predicted PDs, allowing us to compute credible intervals and quantify uncertainty.  
   - Evaluated with the same metrics as the manual logistic model, plus **posterior‑based uncertainty summaries**.

In addition, we use:

- A **scikit‑learn logistic regression** model as a **baseline reference**, not as a formal project “method.”  
  - It provides a conventional benchmark for performance and calibration on the Taiwan dataset.  
  - It is also used to validate that our manual implementation is behaving as expected.

## Phase I: Baseline analysis

Phase I of the project focuses on:

- **Literature review**  
  - Conventional logistic regression in credit scoring.  
  - Ensemble methods and feature selection as prior work (e.g., stacked models on Australian/German/Taiwan data).  
  - Bayesian logistic regression and uncertainty‑aware approaches to credit risk.  
  - Our project framing: comparing frequentist and Bayesian logistic classifiers with an emphasis on calibration and uncertainty.

- **Baseline model (Taiwan dataset)**  
  - EDA: feature types, summary statistics, class balance (≈22% defaults).  
  - Train–test split: 80/20 stratified to preserve the default rate in both sets.  
  - Feature scaling with `StandardScaler`.  
  - scikit‑learn logistic regression:
    - Test AUC ≈ 0.71.  
    - High recall for non‑default, low recall for default.  
    - Calibration curve showing reasonably good average calibration, with mild underestimation of risk at higher predicted PDs.

This baseline establishes a reference point for the manual and Bayesian models that will be implemented in later phases.

## Repository structure

```text
credit-default-ml-project/
├─ README.md              # Project overview and instructions (this file)
├─ data/
│  └─ .gitkeep            # Data are loaded directly from external URLs
├─ notebooks/
│  └─ phase1_baseline_taiwan.ipynb
│       # Phase I notebook:
│       # - Load Taiwan dataset from UCI
│       # - EDA and summary statistics
│       # - Train–test split and scaling
│       # - Baseline scikit-learn logistic regression
│       # - Calibration curve and interpretation
├─ src/
│  └─ (to be added)
│       # manual logistic implementation (Python)
│       # Bayesian model (R)
└─ reports/
   └─ (to be added along with the final poster)
```

## Environment and dependencies

Phase I uses:

- **Python 3.10+**  
- Required packages:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`

As the project moves forward, we will add:

- The **manual logistic regression implementation** (Python) to `src/` and/or a new notebook.  
- The **Bayesian logistic regression** analysis (R), likely in a separate `.Rmd` or notebook.  
- Final evaluation, calibration, and uncertainty comparisons, plus the report and poster files in `reports/`.
