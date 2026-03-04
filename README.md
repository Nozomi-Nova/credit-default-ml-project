# Credit Risk Prediction with Classical, Bayesian, and Ensemble Methods

## Project Overview

This repository contains a multi-phase project on predicting credit default risk using structured tabular data from public credit datasets. Phase I focuses on building a clean, reproducible baseline pipeline using classical machine learning methods on the Taiwan Credit Card Default dataset, with the German Credit dataset as an optional extension in later phases.

The same repository will be extended in future phases to include Bayesian models and ensemble methods, along with additional analysis and reports.

## Datasets

- **Taiwan Credit Card Default (UCI)**  
  Main dataset used. The notebook loads this dataset directly from an online source (no raw data is stored in the `data/` folder).

- **German Credit (UCI, optional)**  
  May be used post Phase 1 to compare model performance across datasets.

For Phase I, the data are loaded by URL inside the notebook, so the `data/` directory remains empty except for a placeholder file and a note.

## Repository Structure

The repository is organized to support Phase I now and additional phases later:

- `README.md` – Project description and instructions.
- `data/` – Placeholder folder; UCI datasets are **loaded directly by URL** in the notebooks.
- `notebooks/`
  - `phase1_baseline_taiwan.ipynb` – Phase I notebook: EDA, preprocessing, and baseline logistic regression on the Taiwan dataset.
  - (Later) other notebooks for Bayesian and ensemble methods.
- `src/` – Reserved for reusable source code (e.g., data loaders, model classes, training scripts) that will be added post Phase 1.
- `reports/` – Future PDF reports and posters.

## Environment and Dependencies

### Python Version

- Recommended: **Python 3.10+**

### Required Packages

The Phase I notebook currently imports the following libraries:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
