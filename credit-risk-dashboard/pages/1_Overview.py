"""Page 1: Overview — project summary, key findings, dataset description."""

import streamlit as st
from data.embedded_data import dataset
from utils.styles import inject_custom_css

st.set_page_config(page_title="Overview — Credit Risk Dashboard", layout="wide")
inject_custom_css()

# ── Header ──────────────────────────────────────────────────────────────────
st.title("Predicting Credit Card Default: Classical vs. Bayesian Logistic Regression")
st.markdown("**Fan Du & Nozomi Kaneda** · DS4420 · Dr. Eric Gerber · Northeastern University · April 2026")
st.markdown("---")

# ── Research Question ───────────────────────────────────────────────────────
st.info(
    "**Research Question:** Does Bayesian posterior inference produce better-calibrated "
    "default probabilities than frequentist logistic regression — and if not, is the "
    "miscalibration statistical (fixable with a better prior) or structural "
    "(inherent in the logistic functional form)?"
)

# ── Key Findings ────────────────────────────────────────────────────────────
st.header("Key Findings")
c1, c2 = st.columns(2)
with c1:
    st.metric("AUC (all three models)", "0.747")
    st.caption("Discrimination is identical across models.")
with c2:
    st.metric("ECE (Frequentist & Bayesian)", "0.054")
    st.caption("Calibration does not improve with Bayesian inference.")

c3, c4 = st.columns(2)
with c3:
    st.metric("ECE with Class Weighting", "0.198", delta="+ 0.144 (3.7x worse)", delta_color="inverse")
    st.caption("Class weighting increased ECE by 3.7\u00d7 \u2014 miscalibration is structural.")
with c4:
    st.metric("Bayesian Coefficients with CI Crossing Zero", "6 of 17")
    st.caption("The Bayesian model honestly quantifies parameter uncertainty.")

# ── Dataset Summary ─────────────────────────────────────────────────────────
st.header("Dataset Summary")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"**Source:** {dataset['name']}")
    st.markdown(f"{dataset['source']}")
    st.markdown(f"**Region:** {dataset['region']}")
with col2:
    st.markdown(f"**Observations:** {dataset['n_total']:,}")
    st.markdown(f"**Default rate:** {dataset['default_rate']:.1%} ({dataset['n_default']:,} / {dataset['n_non_default']:,})")
    st.markdown(f"**Features:** {dataset['n_features']} after preprocessing")
with col3:
    st.markdown(f"**Excluded:** {dataset['excluded']}")
    st.markdown(f"**Train/Test split:** {dataset['split']} ({dataset['train_size']:,} / {dataset['test_size']:,})")

# ── Methodology ─────────────────────────────────────────────────────────────
st.header("Methodology")
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown("#### Manual Logistic Regression")
    st.markdown(
        "Python/NumPy implementation. Full-batch gradient descent, "
        "learning rate = 0.01, convergence at |\u0394L| < 10\u207b\u2076."
    )
with m2:
    st.markdown("#### Class-Weighted LR")
    st.markdown(
        "Same architecture with inverse-frequency weights: "
        "w\u2080 = 0.642, w\u2081 = 2.260. Designed to boost recall on defaults."
    )
with m3:
    st.markdown("#### Bayesian Logistic Regression")
    st.markdown(
        "R/RStan via HMC-NUTS. Priors: Normal(0, 10) intercept, "
        "Normal(0, 2.5) coefficients. 4 chains \u00d7 2,000 iterations."
    )

# ── Footer ──────────────────────────────────────────────────────────────────
st.markdown("---")
st.caption("DS4420 \u00b7 Fan Du & Nozomi Kaneda \u00b7 Northeastern University \u00b7 April 2026")
