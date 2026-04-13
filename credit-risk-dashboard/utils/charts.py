"""Plotly chart helper functions for the Credit Risk Dashboard."""

import math

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def _beta_pdf(x: np.ndarray, a: float, b: float) -> np.ndarray:
    """Beta distribution PDF using pure numpy (avoids scipy dependency)."""
    log_norm = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    log_pdf = log_norm + (a - 1) * np.log(x) + (b - 1) * np.log(1 - x)
    return np.exp(log_pdf)

from data.embedded_data import (
    COLOR_MANUAL, COLOR_WEIGHTED, COLOR_BAYESIAN, COLOR_GOOD,
    mean_pred_freq, frac_pos_freq,
    mean_pred_weighted, frac_pos_weighted,
    mean_pred_bayes, frac_pos_bayes,
    ci_widths,
)


def reliability_diagram() -> go.Figure:
    """Interactive reliability diagram with three model curves."""
    fig = go.Figure()

    # Perfect calibration diagonal
    fig.add_trace(go.Scatter(
        x=[0, 1], y=[0, 1],
        mode="lines",
        line=dict(dash="dash", color="grey", width=1.5),
        name="Perfect Calibration",
        hoverinfo="skip",
    ))

    # Manual LR
    fig.add_trace(go.Scatter(
        x=mean_pred_freq, y=frac_pos_freq,
        mode="lines+markers",
        name="Manual LR",
        line=dict(color=COLOR_MANUAL, width=2.5),
        marker=dict(size=7),
        hovertemplate="Mean pred: %{x:.3f}<br>Fraction pos: %{y:.3f}<extra>Manual LR</extra>",
    ))

    # Weighted LR
    fig.add_trace(go.Scatter(
        x=mean_pred_weighted, y=frac_pos_weighted,
        mode="lines+markers",
        name="Weighted LR",
        line=dict(color=COLOR_WEIGHTED, width=2.5),
        marker=dict(size=7),
        hovertemplate="Mean pred: %{x:.3f}<br>Fraction pos: %{y:.3f}<extra>Weighted LR</extra>",
    ))

    # Bayesian LR with error bars (CI width)
    half_ci = [w / 2 for w in ci_widths]
    fig.add_trace(go.Scatter(
        x=mean_pred_bayes, y=frac_pos_bayes,
        mode="lines+markers",
        name="Bayesian LR",
        line=dict(color=COLOR_BAYESIAN, width=2.5),
        marker=dict(size=7),
        error_y=dict(type="data", array=half_ci, visible=True, color=COLOR_BAYESIAN, thickness=1.5),
        hovertemplate="Mean pred: %{x:.3f}<br>Fraction pos: %{y:.3f}<br>CI width: %{error_y.array:.3f}<extra>Bayesian LR</extra>",
    ))

    fig.update_layout(
        xaxis_title="Mean Predicted Probability",
        yaxis_title="Fraction of Positives (Observed)",
        xaxis=dict(range=[0, 1], dtick=0.1),
        yaxis=dict(range=[0, 1], dtick=0.1),
        legend=dict(x=0.02, y=0.98, bgcolor="rgba(255,255,255,0.8)"),
        height=520,
        margin=dict(l=60, r=30, t=40, b=60),
        plot_bgcolor="white",
        hovermode="closest",
    )
    fig.update_xaxes(showgrid=True, gridcolor="#eee", zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor="#eee", zeroline=False)
    return fig


def ece_mce_bar_chart() -> go.Figure:
    """Grouped bar chart comparing ECE and MCE across models."""
    models = ["Manual LR", "Weighted LR", "Bayesian LR"]
    ece_vals = [0.0541, 0.1977, 0.0543]
    mce_vals = [0.2053, 0.2985, 0.2003]
    colors = [COLOR_MANUAL, COLOR_WEIGHTED, COLOR_BAYESIAN]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=models, y=ece_vals, name="ECE",
        marker_color=[c if v < 0.10 else "#CC0000" for c, v in zip(colors, ece_vals)],
        text=[f"{v:.4f}" for v in ece_vals], textposition="outside",
        hovertemplate="%{x}<br>ECE = %{y:.4f}<extra></extra>",
    ))
    fig.add_trace(go.Bar(
        x=models, y=mce_vals, name="MCE",
        marker_color=[c if v < 0.25 else "#CC0000" for c, v in zip(colors, mce_vals)],
        text=[f"{v:.4f}" for v in mce_vals], textposition="outside",
        hovertemplate="%{x}<br>MCE = %{y:.4f}<extra></extra>",
    ))

    fig.update_layout(
        barmode="group",
        yaxis_title="Calibration Error",
        yaxis=dict(range=[0, 0.38]),
        legend=dict(x=0.02, y=0.98),
        height=400,
        margin=dict(l=60, r=30, t=30, b=60),
        plot_bgcolor="white",
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor="#eee")
    return fig


def posterior_density_plot(profile: dict) -> go.Figure:
    """
    Plot a posterior predictive density for a single borrower.
    Approximates using a Beta distribution fitted to the posterior mean and CI.
    """
    mean = profile["posterior_mean"]
    ci_lo = profile["ci_low"]
    ci_hi = profile["ci_high"]
    freq = profile["freq_estimate"]
    true_outcome = profile["true_outcome"]
    true_label = profile["true_label"]

    # Fit a Beta distribution: match mean and approximate variance from CI
    ci_width = ci_hi - ci_lo
    # For a 95% CI, width ~ 2*1.96*std, so std ~ width/3.92
    std_approx = ci_width / 3.92
    var_approx = std_approx ** 2

    # Beta parameters from mean and variance
    # mean = a/(a+b), var = ab/((a+b)^2*(a+b+1))
    if var_approx > 0 and mean > 0 and mean < 1:
        common = mean * (1 - mean) / var_approx - 1
        a = max(mean * common, 1.01)
        b = max((1 - mean) * common, 1.01)
    else:
        a, b = 2, 2

    x = np.linspace(max(0.001, ci_lo - 0.15), min(0.999, ci_hi + 0.15), 500)
    y = _beta_pdf(x, a, b)

    fig = go.Figure()

    # Shaded 95% CI region
    ci_mask = (x >= ci_lo) & (x <= ci_hi)
    x_ci = x[ci_mask]
    y_ci = y[ci_mask]
    fig.add_trace(go.Scatter(
        x=np.concatenate([x_ci, x_ci[::-1]]),
        y=np.concatenate([y_ci, np.zeros_like(y_ci)]),
        fill="toself",
        fillcolor="rgba(255,140,0,0.2)",
        line=dict(width=0),
        name="95% CI",
        hoverinfo="skip",
    ))

    # Posterior density curve
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode="lines",
        name="Posterior Density",
        line=dict(color=COLOR_BAYESIAN, width=2.5),
        hovertemplate="P(default) = %{x:.3f}<br>Density = %{y:.2f}<extra></extra>",
    ))

    y_max = max(y) * 1.1

    # Decision threshold
    fig.add_vline(x=0.5, line=dict(dash="dash", color="grey", width=1.5),
                  annotation_text="Threshold (0.5)", annotation_position="top right",
                  annotation_font_size=10)

    # Posterior mean
    fig.add_vline(x=mean, line=dict(dash="dash", color=COLOR_BAYESIAN, width=2),
                  annotation_text=f"Post. Mean = {mean:.3f}", annotation_position="top left",
                  annotation_font_size=10)

    # Frequentist point estimate
    fig.add_vline(x=freq, line=dict(color=COLOR_MANUAL, width=2),
                  annotation_text=f"Freq. Est. = {freq:.3f}", annotation_position="bottom right",
                  annotation_font_size=10)

    # True outcome annotation
    outcome_color = "#CC0000" if true_outcome == 1 else COLOR_GOOD
    fig.add_annotation(
        x=0.98, y=0.95, xref="paper", yref="paper",
        text=f"True: {true_label}",
        showarrow=False,
        font=dict(size=13, color=outcome_color, family="sans-serif"),
        bgcolor="rgba(255,255,255,0.8)",
        bordercolor=outcome_color,
        borderwidth=1,
        borderpad=4,
    )

    fig.update_layout(
        xaxis_title="P(Default)",
        yaxis_title="Density",
        height=420,
        margin=dict(l=50, r=30, t=40, b=50),
        plot_bgcolor="white",
        showlegend=True,
        legend=dict(x=0.02, y=0.98, bgcolor="rgba(255,255,255,0.8)"),
    )
    fig.update_xaxes(showgrid=True, gridcolor="#eee", zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor="#eee", zeroline=False)
    return fig
