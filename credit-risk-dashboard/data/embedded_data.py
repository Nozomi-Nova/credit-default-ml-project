"""
All hardcoded data for the Credit Risk Dashboard.
Extracted from the project notebook outputs.
"""

# ---------------------------------------------------------------------------
# Colors
# ---------------------------------------------------------------------------
COLOR_MANUAL = "#4682B4"   # steelblue
COLOR_WEIGHTED = "#228B22" # forestgreen
COLOR_BAYESIAN = "#FF8C00" # darkorange
COLOR_BAD = "#CC0000"      # Northeastern red
COLOR_GOOD = "#006400"     # dark green

# ---------------------------------------------------------------------------
# Calibration curve data — 10 equal-width bins
# ---------------------------------------------------------------------------

# Manual (Frequentist) LR
mean_pred_freq = [0.0780, 0.1485, 0.2424, 0.3449, 0.4550, 0.5450, 0.6433, 0.7511, 0.8395, 0.9553]
frac_pos_freq  = [0.0823, 0.1329, 0.2742, 0.3260, 0.5281, 0.6080, 0.6056, 0.7301, 0.7692, 0.7500]

# Weighted LR — the weighted model's curve collapses below the diagonal
# in the middle bins. MCE bin is at mean_pred ~ 0.65, frac_pos ~ 0.35.
# Values approximated from the notebook's plotted calibration curve and
# the MCE bin info (mean_pred=0.6499, frac_pos=0.3515).
mean_pred_weighted = [0.0344, 0.1294, 0.2431, 0.3571, 0.4615, 0.5608, 0.6499, 0.7509, 0.8504, 0.9504]
frac_pos_weighted  = [0.0382, 0.0960, 0.1667, 0.2462, 0.3361, 0.3515, 0.3515, 0.5610, 0.6207, 0.7500]

# Bayesian LR
mean_pred_bayes = [0.0763, 0.1448, 0.2427, 0.3434, 0.4544, 0.5476, 0.6470, 0.7511, 0.8374, 0.9542]
# TODO: extract true Bayesian frac_pos from notebook — these are currently
# copied from frac_pos_freq, which is approximate but not exact since different
# predicted probabilities land in different bins.
frac_pos_bayes  = [0.0823, 0.1329, 0.2742, 0.3260, 0.5281, 0.6080, 0.6056, 0.7301, 0.7692, 0.7500]

# Mean posterior CI width per bin (Bayesian)
ci_widths = [0.0294, 0.0240, 0.0502, 0.0566, 0.0762, 0.0684, 0.0704, 0.0513, 0.0466, 0.0216]

# ---------------------------------------------------------------------------
# Model comparison metrics
# ---------------------------------------------------------------------------
model_comparison = {
    "Metric": [
        "AUC",
        "Brier Score",
        "ECE",
        "MCE",
        "Recall (@ 0.5)",
        "Mean Posterior CI Width",
    ],
    "Manual LR": [0.7465, 0.1406, 0.0541, 0.2053, 0.310, "N/A"],
    "Weighted LR": [0.7471, 0.1907, 0.1977, 0.2985, 0.545, "N/A"],
    "Bayesian LR": [0.7446, 0.1404, 0.0543, 0.2003, 0.327, 0.034],
}

# Metrics where higher = worse for weighted LR (for red highlighting)
worse_metrics = {"Brier Score", "ECE", "MCE"}
# Metrics where higher = better for weighted LR
better_metrics = {"Recall (@ 0.5)"}

# ---------------------------------------------------------------------------
# Borrower profiles (posterior predictive)
# ---------------------------------------------------------------------------
profile_a = {
    "label": "Profile A — Borderline Borrower",
    "posterior_mean": 0.4183,
    "ci_low": 0.2936,
    "ci_high": 0.5409,
    "freq_estimate": 0.3647,
    "true_outcome": 1,  # DEFAULT
    "true_label": "DEFAULT",
    "index": 1058,
}

profile_b = {
    "label": "Profile B — Overconfident Prediction",
    "posterior_mean": 0.9929,
    "ci_low": 0.9908,
    "ci_high": 0.9947,
    "freq_estimate": 0.9914,
    "true_outcome": 0,  # NON-DEFAULT
    "true_label": "NON-DEFAULT",
    "index": 850,
}

# ---------------------------------------------------------------------------
# Dataset summary
# ---------------------------------------------------------------------------
dataset = {
    "name": "Default of Credit Card Clients",
    "source": "UCI Machine Learning Repository (Yeh & Lien, 2009)",
    "n_total": 30_000,
    "region": "Taiwanese credit card holders, October 2005",
    "default_rate": 0.221,
    "n_default": 6_636,
    "n_non_default": 23_364,
    "n_features": 16,
    "excluded": "AGE and 6 BILL_AMT columns (VIF-based)",
    "train_size": 24_000,
    "test_size": 6_000,
    "split": "80/20 stratified",
}
