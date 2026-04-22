# 🚴 Forecasting Hourly Bike‑Sharing Demand for Sustainable Urban Mobility

This project builds a regression model to predict **hourly bike rental demand** using weather and time‑of‑day information from the Bike Sharing dataset. The goal is to support better fleet allocation in bike‑sharing systems and help cities promote low‑carbon transport options.

## 🤔 Problem and Hypothesis

We predict `cnt` (total hourly rentals) using features such as hour of the day (`hr`), weather conditions (`weathersit`, `temp`, `hum`, `windspeed`), and calendar variables (`weekday`, `workingday`, `season`).  
My hypothesis is that **hour of the day and weather conditions influence hourly demand**, with the highest usage during peak commuting hours on clear, mild days and lower demand during extreme weather or late‑night hours.

## 📊 Dataset

- **Source:** UCI Bike Sharing dataset (hourly file)  
  https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset
- **What it contains:**
  - `hour.csv` with hourly records of bike rentals (2011–2012, Washington, D.C.).
  - Target: `cnt` (total rentals per hour).
  - Features: `hr`, `season`, `yr`, `mnth`, `weekday`, `workingday`, `holiday`, `weathersit`, `temp`, `hum`, `windspeed`, etc.
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

## 👨‍💻 Usage

1. Place `hour.csv` in `data/raw/`.
2. Run the notebook:
   - `notebooks/regression_capstone.ipynb`  
     (or `jupyter lab notebooks/regression_capstone.ipynb` if you prefer).
3. The notebook will:
   - Load the data from `data/raw/`.
   - Perform preprocessing and modeling.
   - Save figures to `outputs/figures/` and results to `outputs/reports/`.

## 📂 Folder Structure

- `data/raw/` – Original `hour.csv`
- `data/processed/` – Cleaned and feature‑engineered versions.
- `notebooks/` – Main regression notebook.
- `src/utils.py` – Helper functions for preprocessing.
- `outputs/figures/` – Plots showing model performance.
- `outputs/reports/` – Evaluation summaries.
- `requirements.txt` – Package dependencies.

## 📝 Ethical and Sustainability Notes

- Predictions are intended to support **equitable fleet allocation** and improve service quality for all riders.
- The model does not use personal or sensitive data; it is based on aggregate, time‑series records.
- Any model outputs should be used as **a decision‑support tool**, not as a justification for reducing service in underserved areas.

## 🖇️ Dependencies

Listed in `requirements.txt`

## 💁🏻‍♀️ Contact

Clarisse Casi Cariño (casi.carino.business@gmail.com)
