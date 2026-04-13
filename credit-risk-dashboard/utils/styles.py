"""Northeastern-themed CSS injection for the Credit Risk Dashboard."""

import streamlit as st

_BANNER_HTML = """
<div style="background-color: #000000; padding: 10px 20px; border-bottom: 3px solid #CC0000;
            margin: -1rem -1rem 1.5rem -1rem; border-radius: 0;">
    <span style="color: #FFFFFF; font-size: 0.95rem; font-weight: 600; letter-spacing: 0.5px;">
        DS4420 &middot; Credit Risk Dashboard
    </span>
    <span style="color: #999999; font-size: 0.8rem; float: right;">
        Fan Du &amp; Nozomi Kaneda &middot; Northeastern University
    </span>
</div>
"""

_CSS = """
<style>
/* ── Dark sidebar ──────────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background-color: #1A1A1A;
}
[data-testid="stSidebar"] * {
    color: #F0F0F0 !important;
}
[data-testid="stSidebar"] hr {
    border-color: #333 !important;
}

/* ── Red accent on active sidebar page ─────────────────────────────────── */
[data-testid="stSidebar"] a[aria-selected="true"],
[data-testid="stSidebar"] .st-emotion-cache-1cypcdb {
    border-left: 3px solid #CC0000 !important;
    background-color: rgba(204, 0, 0, 0.1) !important;
}

/* ── Section header red left-border ────────────────────────────────────── */
.main h2 {
    border-left: 4px solid #CC0000;
    padding-left: 12px;
}

/* ── Metric card polish ────────────────────────────────────────────────── */
[data-testid="stMetric"] {
    background-color: #F7F7F7;
    border: 1px solid #E0E0E0;
    border-top: 3px solid #CC0000;
    border-radius: 6px;
    padding: 16px;
}
</style>
"""


def inject_custom_css():
    """Inject Northeastern-themed CSS and top banner into the page."""
    st.markdown(_CSS, unsafe_allow_html=True)
    st.markdown(_BANNER_HTML, unsafe_allow_html=True)
