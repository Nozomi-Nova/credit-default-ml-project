# Credit Risk Dashboard — DS4420 Extra Credit

**Fan Du & Nozomi Kaneda** · DS4420 · Dr. Eric Gerber · Northeastern University · April 2026

An interactive Streamlit dashboard comparing classical (frequentist), class-weighted, and Bayesian logistic regression for credit card default prediction.

## Live App

🔗 **[credit-risk-ds4420.streamlit.app](https://credit-risk-ds4420.streamlit.app)** *(update this URL after deployment)*

## Pages

| Page | Description |
|------|-------------|
| **Home** | Project overview and navigation |
| **Overview** | Key findings, dataset summary, and methodology |
| **Calibration Analysis** | Interactive reliability diagram, ECE/MCE comparison, and full model comparison table |
| **Borrower Profiles** | Posterior predictive density plots for two individual borrowers |

## Run Locally

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/credit-risk-dashboard.git
cd credit-risk-dashboard

# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py
```

The app will open at `http://localhost:8501`.

## Deploy to Streamlit Community Cloud

1. Push this repo to GitHub (public repository).
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **Create app** → **Yup, I have an app**.
4. Select this repository, branch `main`, and main file path `app.py`.
5. (Optional) Set a custom subdomain like `credit-risk-ds4420`.
6. Click **Deploy**.

The app should be live within a few minutes.

## Tech Stack

- **Streamlit** — app framework
- **Plotly** — interactive charts
- **NumPy / Pandas** — data handling
- All data is embedded in `data/embedded_data.py` (no external data files needed).

## Data Source

Yeh, I. C., & Lien, C. H. (2009). The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients. *Expert Systems with Applications*, 36(2), 2473–2480. [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients).
