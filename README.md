# Diabetes Hospital Big Data Analytics

Analysis of the UCI Diabetes 130-US Hospitals dataset (~101,766 patient records) covering hospital stay duration, readmission prediction, and OLAP reporting.

## Project Structure

```
├── notebooks/
│   ├── 00_data_preparation.ipynb       # Merges discharge_disposition_id into cleaned dataset
│   ├── 01_exploratory_analysis.ipynb   # Initial EDA — distributions, correlations, box plots
│   ├── 02_descriptive_analysis.ipynb   # Full pipeline — EDA, regression (MNLogit), logistic classification
│   └── 03_tas_dataset_analysis.ipynb   # Alternate dataset — Naive Bayes, correlation analysis
├── dashboard/
│   ├── olap_report.py                  # Interactive Dash app (port 8053)
│   └── olap_report_outlined.py         # Dash app variant with bar outlines (port 8054)
├── data/                               # Place your CSV files here (not committed — see below)
├── requirements.txt
└── .gitignore
```

## Setup

```bash
pip install -r requirements.txt
```

## Data Files

The CSV data files are not included in this repository (patient data). Place them in the `data/` folder before running:

| File | Used by |
|---|---|
| `diabetic_data.csv` | 00, 01 notebooks |
| `cleaned_diabetic_data_with_Median.csv` | 00 notebook |
| `updated cleaned_diabetic_data_with_Median.csv` | 02 notebook |
| `cleaned_diabetic_data_with_Median 1.csv` | Dashboard |
| `diabetic_data_Tas.csv` | 03 notebook |

Run `00_data_preparation.ipynb` first — it generates `updated cleaned_diabetic_data_with_Median.csv` from the raw files.

## Running the Notebooks

Open Jupyter and run each notebook top-to-bottom in numbered order:

```bash
jupyter lab
```

## Running the Dashboard

```bash
python dashboard/olap_report.py
# Open http://localhost:8053
```

To enable the debug mode:
```bash
DASH_DEBUG=true python dashboard/olap_report.py
```

## Requirements

- Python 3.10+
- See `requirements.txt` for all dependencies
