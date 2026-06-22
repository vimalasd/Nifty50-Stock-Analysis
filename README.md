# 📈 Nifty 50 Stock Analysis Dashboard

A Stock Market Analytics Dashboard built using Python, Pandas, SQLite, Streamlit, Matplotlib, and Seaborn to analyze Nifty 50 stock performance and generate actionable financial insights.

---

## Project Overview

This project analyzes Nifty 50 stock data by calculating key financial metrics such as returns, volatility, sector performance, correlations, and monthly trends, and presents the insights through an interactive Streamlit dashboard.

---

## Features

### Market Overview

- Top 10 Green Stocks (Highest Returns)
- Top 10 Red Stocks (Lowest Returns)
- Market Summary Metrics
- Average Stock Price
- Average Trading Volume

### Volatility Analysis

- Daily Return Calculation
- Volatility Measurement
- Top 10 Most Volatile Stocks
- Volatility Comparison Charts

### Cumulative Return Analysis

- Cumulative Return Calculation
- Top 5 Performing Stocks
- Performance Trend Visualization

### Sector Performance Analysis

- Sector-wise Stock Mapping
- Average Yearly Return by Sector
- Sector Comparison

### Stock Correlation Analysis

- Correlation Matrix Generation
- Correlation Heatmap
- Top Correlated Stock Pairs

### Monthly Gainers & Losers

- Monthly Return Calculation
- Top 5 Monthly Gainers
- Top 5 Monthly Losers
- Monthly Performance Comparison

---

## Workflow

### 1. Data Extraction

- Read stock data from YAML files
- Convert data into Pandas DataFrames
- Create separate stock-wise CSV files

### 2. Data Cleaning & Transformation

- Handle date formatting
- Sort data by stock and date
- Convert columns to appropriate data types
- Prepare data for analysis

### 3. Financial Analysis

Performed the following calculations:

- Yearly Return
- Daily Return
- Volatility
- Cumulative Return
- Monthly Return
- Sector Performance
- Stock Correlation

### 4. Database Creation

- Store analysis results in SQLite database
- Create separate tables for each analysis module

### 5. Streamlit Dashboard

Interactive dashboard with multiple analysis pages and visualizations.

---

## Dashboard Pages

### Market Overview

Displays:

- Market Summary
- Top 10 Green Stocks
- Top 10 Red Stocks

### Volatility Analysis

Displays:

- Top 10 Volatile Stocks
- Volatility Bar Chart

### Cumulative Return Analysis

Displays:

- Top 5 Performing Stocks
- Cumulative Return Trend Chart

### Sector Performance

Displays:

- Average Sector Returns
- Sector Comparison Chart

### Stock Correlation

Displays:

- Correlation Heatmap
- Top Correlated Stock Pairs

### Monthly Gainers & Losers

Displays:

- Monthly Top Gainers
- Monthly Top Losers
- Monthly Performance Charts

---

## Technology Stack

- Python
- Pandas
- SQLite
- Streamlit
- Matplotlib
- Seaborn
- PyYAML

---

## Project Structure

```text
data/
├── ticker_csvs/
└── yaml_files/

Sector_data.csv
analysis.db

app.py
stock_analysis.ipynb
yaml_to_csv.py


README.md
```

| File / Folder | Purpose |
|--------|---------|
| `data/yaml_files/` | Raw stock data in YAML format |
| `data/ticker_csvs/`|  Stock-wise csv files |
| `Sector_data.csv` | Sector mapping file |
| `yaml_to_csv.py` | Extracts YAML data and creates stock CSV files |
| `stock_analysis.ipynb` | Stock analysis and stores results in SQLite |
| `analysis.db` | SQLite database|
| `app.py` | Streamlit dashboard application |
| `README.md` | Project documentation |

---

## Installation

Install dependencies:

```bash
pip install pandas matplotlib seaborn streamlit pyyaml
```

Run the dashboard:

```bash
streamlit run app.py
```

Once the application starts, Streamlit displays a local URL such as:

```text
http://localhost:8501
```

open it in your browser.

---

## Skills Demonstrated

- Data Extraction
- Data Cleaning
- Data Transformation
- Financial Data Analysis
- Correlation Analysis
- Data Visualization
- Streamlit Dashboard Development

---

## Business Value

- Identifies top-performing stocks
- Measures stock volatility and risk
- Tracks long-term stock performance
- Compares sector-wise performance
- Detects highly correlated stocks
- Analyzes monthly market trends


---
