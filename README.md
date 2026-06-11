# Mutual Fund Analytics Capstone Project

## Overview

This project was developed as part of the Bluestock Fintech Mutual Fund Analytics Capstone. The objective was to build a complete end-to-end analytics solution covering data ingestion, ETL processing, exploratory data analysis, performance analytics, dashboard development, and advanced investor analytics.

The project analyzes mutual fund industry trends, fund performance, investor behavior, SIP patterns, and portfolio concentration using Python, SQLite, Jupyter Notebook, and Power BI.

---

## Project Objectives

* Build an automated ETL pipeline
* Clean and transform raw mutual fund datasets
* Store processed data in SQLite
* Perform exploratory data analysis (EDA)
* Compute fund performance metrics
* Develop an interactive Power BI dashboard
* Perform advanced investor and risk analytics
* Deliver a complete analytics report and presentation

---

## Technology Stack

* Python
* Pandas
* NumPy
* Matplotlib
* SQLite
* Jupyter Notebook
* Power BI
* Git & GitHub

---

## Project Structure

```text
mutual_fund_analysis/

├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   ├── Dashboard.pdf
│   └── Dashboard Screenshots
│
├── reports/
│   ├── var_cvar_report.csv
│   ├── rolling_sharpe_chart.png
│   └── Final_Report.pdf
│
├── sql/
│
├── recommender.py
├── run_pipeline.py
└── README.md
```

---

## Completed Tasks

### Day 1 – ETL Pipeline

* Data ingestion
* Raw data validation
* Project structure setup

### Day 2 – Data Cleaning & Database

* Data cleaning
* Missing value treatment
* SQLite database creation

### Day 3 – Exploratory Data Analysis

* Industry trends analysis
* Fund category analysis
* Investor behavior analysis
* Visualizations and insights

### Day 4 – Performance Metrics

* Sharpe Ratio
* Beta
* Historical VaR
* Conditional VaR (CVaR)
* Risk analysis

### Day 5 – Power BI Dashboard

* Industry Overview
* Fund Performance
* Investor Analytics
* SIP & Market Trends

### Day 6 – Advanced Analytics

* Rolling 90-Day Sharpe
* Investor Cohort Analysis
* SIP Continuity Analysis
* Fund Recommendation Engine
* Sector HHI Concentration Analysis

### Day 7 – Final Documentation

* Final project report
* Presentation deck
* GitHub repository cleanup
* Project deployment preparation

---

## Dashboard Features

* Industry KPI monitoring
* Fund performance comparison
* Risk vs return analysis
* Investor demographic insights
* SIP trend analysis
* Category inflow tracking

---

## Key Findings

* Funds with higher Sharpe ratios delivered superior risk-adjusted returns.
* SIP inflows demonstrated consistent growth over the analysis period.
* Certain investor cohorts contributed significantly higher investments.
* SIP continuity analysis identified at-risk investors.
* Portfolio concentration varied substantially across equity funds.

---

## Running the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL Pipeline

```bash
python run_pipeline.py
```

### Open Dashboard

Open:

```text
dashboard/bluestock_mf_dashboard.pbix
```

using Power BI Desktop.

---

## Deliverables

* ETL Pipeline
* SQLite Database
* EDA Notebook
* Performance Analytics Notebook
* Advanced Analytics Notebook
* Power BI Dashboard
* Final Project Report
* Presentation Deck

---

## Author

Karthikeya

Bluestock Fintech Capstone Project

