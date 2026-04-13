"""
Credit Risk Dashboard — DS4420 Extra Credit
Fan Du & Nozomi Kaneda · Northeastern University · April 2026
"""

import streamlit as st
from utils.styles import inject_custom_css

st.set_page_config(
    page_title="Credit Risk Dashboard — DS4420",
    page_icon=":bar_chart:",
    layout="wide",
)
inject_custom_css()

st.title("Predicting Credit Card Default")
st.subheader("Classical vs. Bayesian Logistic Regression")
st.markdown(
    "This dashboard explores whether Bayesian posterior inference produces "
    "better-calibrated default probabilities than classical logistic regression. "
    "Navigate using the sidebar to explore model performance, calibration analysis, "
    "and individual borrower profiles."
)

# ── Navigation cards ────────────────────────────────────────────────────────
c1, c2, c3 = st.columns(3)

_card = (
    '<div style="background:#F7F7F7; border-left:4px solid #CC0000; '
    'padding:16px 20px; border-radius:4px; height:100%">'
    '<p style="font-weight:700; margin:0 0 6px 0; font-size:1.05rem">{title}</p>'
    '<p style="margin:0; color:#555; font-size:0.9rem">{desc}</p></div>'
)

with c1:
    st.markdown(
        _card.format(title="Overview", desc="Project summary, key findings, and dataset description."),
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        _card.format(title="Calibration Analysis", desc="Reliability diagrams, ECE/MCE comparison, and model metrics."),
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        _card.format(title="Borrower Profiles", desc="Posterior density plots illustrating Bayesian uncertainty."),
        unsafe_allow_html=True,
    )

# ── Footer ──────────────────────────────────────────────────────────────────
st.markdown("---")
st.caption("DS4420 · Fan Du & Nozomi Kaneda · Northeastern University · April 2026")
