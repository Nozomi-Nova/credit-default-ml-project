"""Page 2: Calibration Analysis — reliability diagram, ECE/MCE, model comparison."""

import streamlit as st
from data.embedded_data import model_comparison, worse_metrics, better_metrics, COLOR_BAD, COLOR_GOOD
from utils.charts import reliability_diagram, ece_mce_bar_chart
from utils.styles import inject_custom_css

st.set_page_config(page_title="Calibration Analysis — Credit Risk Dashboard", layout="wide")
inject_custom_css()

st.title("Calibration Analysis")
st.markdown("Comparing calibration quality across frequentist, weighted, and Bayesian logistic regression.")
st.markdown("---")

# ── Reliability Diagram ────────────────────────────────────────────────────
st.header("Interactive Reliability Diagram")
st.plotly_chart(reliability_diagram(), use_container_width=True)
st.caption(
    "Each point represents one of 10 equal-width probability bins. "
    "The Bayesian error bars show the mean 95% posterior CI width per bin. "
    "Toggle curves on/off by clicking the legend; hover for exact values."
)

# ── ECE / MCE Comparison ───────────────────────────────────────────────────
st.header("ECE / MCE Comparison")
st.plotly_chart(ece_mce_bar_chart(), use_container_width=True)
st.warning(
    "Class weighting **increased ECE by 3.7\u00d7** (0.054 \u2192 0.198) while leaving AUC unchanged "
    "\u2014 confirming **structural miscalibration**."
)

# ── Full Model Comparison Table ─────────────────────────────────────────────
st.header("Full Model Comparison")

metrics = model_comparison["Metric"]
cols = ["Manual LR", "Weighted LR", "Bayesian LR"]
rows_html = ""
for i, metric in enumerate(metrics):
    cells = f"<td style='padding:8px 12px; font-weight:600'>{metric}</td>"
    for col in cols:
        val = model_comparison[col][i]
        cell_text = f"{val:.4f}" if isinstance(val, float) else str(val)
        style = "padding:8px 12px"
        if col == "Weighted LR":
            if metric in worse_metrics:
                style += f"; color:{COLOR_BAD}; font-weight:bold"
            elif metric in better_metrics:
                style += f"; color:{COLOR_GOOD}; font-weight:bold"
        cells += f"<td style='{style}'>{cell_text}</td>"
    rows_html += f"<tr style='border-bottom:1px solid #eee'>{cells}</tr>"

header = "".join(
    f"<th style='padding:10px 12px; text-align:left; color:#fff'>{c}</th>"
    for c in ["Metric"] + cols
)
table_html = f"""
<table style="width:100%; border-collapse:collapse; font-size:0.95rem; border-top:3px solid #CC0000">
<thead><tr style="background-color:#1A1A1A">{header}</tr></thead>
<tbody>{rows_html}</tbody>
</table>
"""
st.markdown(table_html, unsafe_allow_html=True)

# ── Interpretation ──────────────────────────────────────────────────────────
st.header("Interpretation")

with st.expander("Why is ECE identical for frequentist and Bayesian?"):
    st.markdown(
        "At n = 24,000, **likelihood dominance** means the prior (Normal(0, 2.5)) "
        "contributes essentially no information. The posterior is driven entirely by "
        "the data, producing point predictions nearly identical to MLE."
    )

with st.expander("Why does class weighting worsen calibration?"):
    st.markdown(
        "Inverse-frequency weights inflate the loss contribution of minority-class "
        "(default) observations. This shifts the decision boundary toward higher "
        "sensitivity but **distorts the predicted probability surface**, pulling "
        "predictions away from the true conditional probabilities."
    )

with st.expander("What is structural miscalibration?"):
    st.markdown(
        "The logistic model assumes log-odds are linear in the features. When the "
        "true conditional default probability has a **non-linear relationship** with "
        "the feature space, no amount of re-weighting or Bayesian inference can fix "
        "the calibration \u2014 the functional form itself is the bottleneck."
    )

# ── Footer ──────────────────────────────────────────────────────────────────
st.markdown("---")
st.caption("DS4420 \u00b7 Fan Du & Nozomi Kaneda \u00b7 Northeastern University \u00b7 April 2026")
