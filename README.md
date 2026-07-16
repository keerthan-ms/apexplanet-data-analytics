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

---

### Looking at your ApexPlanet Portal
I also noticed your second screenshot of the ApexPlanet portal! 
* **Task 4** says "Submit in process...". Since it is currently past 11:30 PM IST, and their support hours end at 10:00 PM, it will likely be fully approved in the morning.
* **Task 5** is unlocked and ready for your final submission.
* **Certificate:** Just a heads-up, the portal mentions a standard ₹49 platform processing fee to download your final verified certificate once Task 5 is approved.

<FollowUp label="Create the Executive Summary" query="The main README is updated! Let's build the final 2-page Executive Summary PDF for Task 5 so I can submit it."/>
