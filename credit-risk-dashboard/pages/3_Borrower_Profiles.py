"""Page 3: Borrower Profiles — interactive posterior density plots."""

import streamlit as st
from data.embedded_data import profile_a, profile_b
from utils.charts import posterior_density_plot
from utils.styles import inject_custom_css

st.set_page_config(page_title="Borrower Profiles — Credit Risk Dashboard", layout="wide")
inject_custom_css()

st.title("Borrower Profiles: Bayesian Uncertainty in Action")
st.markdown(
    "Individual-level posterior predictive distributions illustrate what Bayesian "
    "inference adds \u2014 and where it falls short."
)
st.markdown("---")

# ── Side-by-side profiles ──────────────────────────────────────────────────
col_a, col_b = st.columns(2)

with col_a:
    st.subheader(profile_a["label"])
    st.plotly_chart(posterior_density_plot(profile_a), use_container_width=True)
    st.markdown(
        f"**Posterior mean:** {profile_a['posterior_mean']:.3f} \u00b7 "
        f"**95% CI:** [{profile_a['ci_low']:.3f}, {profile_a['ci_high']:.3f}] \u00b7 "
        f"**Frequentist:** {profile_a['freq_estimate']:.3f}"
    )
    st.markdown(
        "The CI straddles the 0.5 threshold \u2014 the Bayesian model honestly communicates "
        "that this borrower could go either way. The frequentist point estimate "
        f"({profile_a['freq_estimate']:.3f}) suggests confident non-default."
    )

with col_b:
    st.subheader(profile_b["label"])
    st.plotly_chart(posterior_density_plot(profile_b), use_container_width=True)
    st.markdown(
        f"**Posterior mean:** {profile_b['posterior_mean']:.3f} \u00b7 "
        f"**95% CI:** [{profile_b['ci_low']:.3f}, {profile_b['ci_high']:.3f}] \u00b7 "
        f"**Frequentist:** {profile_b['freq_estimate']:.3f}"
    )
    st.markdown(
        "Both models predict near-certain default. The posterior is extremely narrow "
        f"(CI width = {profile_b['ci_high'] - profile_b['ci_low']:.4f}), meaning the "
        "Bayesian model is **confident in its wrong prediction**. This illustrates "
        "the MCE problem at the individual level."
    )

# ── Key Takeaway ────────────────────────────────────────────────────────────
st.markdown("---")
st.info(
    "**Key Takeaway:** The Bayesian model's contribution is not better predictions \u2014 "
    "it's **honest uncertainty quantification**. Profile A shows the model correctly "
    "flagging ambiguity. Profile B shows that even honest uncertainty can't overcome "
    "structural miscalibration: the model is both confident and wrong."
)

# ── Footer ──────────────────────────────────────────────────────────────────
st.markdown("---")
st.caption("DS4420 \u00b7 Fan Du & Nozomi Kaneda \u00b7 Northeastern University \u00b7 April 2026")
