# 📊 Customer Acquisition & Marketing Performance Analysis
**ApexPlanet Software Pvt Ltd - Data Analytics Internship Project**

## 🎯 Project Objective
This repository contains a full-stack data analytics pipeline developed to evaluate marketing channel efficiency, calculate Customer Acquisition Cost (CAC), and determine the optimal allocation of marketing budgets. 

The analysis proves statistically that **Email Marketing** yields the highest Return on Investment (ROI), while **Paid Advertising** currently operates at a capital deficit requiring immediate strategic auditing.

## 🧰 Tech Stack & Tools
* **Languages:** Python (Pandas, NumPy, SciPy), SQL
* **Visualization:** Looker Studio, Plotly, Matplotlib, Seaborn
* **Techniques:** Exploratory Data Analysis (EDA), Hypothesis Testing (Independent T-Tests), Data Pipeline Automation

## 📂 Repository Structure
* `/dashboards` - Contains the Looker Studio PDF exports, UI screenshots, and interactive Plotly HTML charts.
* `/data` - Contains the raw and cleaned customer acquisition datasets.
* `/notebooks` - Jupyter Notebooks detailing the EDA (Task 1 & 2) and Statistical Hypothesis Testing (Task 4).
* `/reports` - Executive presentation slides outlining key findings and strategic recommendations.
* `/scripts` - Python automation script (`automated_reporting.py`) for automated data cleaning, KPI calculation, and Excel reporting.

## 📈 Key Strategic Insights
1. **Email Marketing Dominance:** Drives the highest efficient revenue with the lowest acquisition cost.
2. **Paid Ad Deficit:** A Cost Independent T-Test ($p$-value: $0.0000$) mathematically proved that Paid Advertising is statistically far more expensive per customer than organic channels, operating at a severe deficit.
3. **Revenue Consistency:** A Revenue Independent T-Test ($p$-value: $0.9933$) confirmed that the quality of customers (gross revenue generated) remains highly consistent regardless of the acquisition channel. 

## 🚀 How to Run the Automation Script
To run the automated data pipeline that generates the KPI Excel report:
```bash
pip install -r requirements.txt
python scripts/automated_reporting.py
