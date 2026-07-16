import pandas as pd
import datetime

def run_data_pipeline():
    print("🚀 Starting Automated Data Pipeline...")
    
    # 1. Load the raw data
    try:
        # Replace with your actual raw data file name if it differs
        df = pd.read_csv('cleaned_customer_acquisition_data.csv')
        print("✅ Data successfully loaded.")
    except FileNotFoundError:
        print("❌ Error: Raw data file not found.")
        return

    # 2. Data Cleaning (Automated steps)
    # Drop duplicates
    df = df.drop_duplicates()
    # Fill missing values (if any) with 0 for numeric columns
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)
    print("✅ Data successfully cleaned.")

    # 3. Calculate Key KPIs by Channel
    kpi_report = df.groupby('channel').agg(
        Total_Revenue=('revenue', 'sum'),
        Total_Cost=('cost', 'sum')
    ).reset_index()

    # Calculate ROI Percentage
    kpi_report['Average_ROI (%)'] = ((kpi_report['Total_Revenue'] - kpi_report['Total_Cost']) / kpi_report['Total_Cost']) * 100
    
    # Round numbers for a clean report
    kpi_report = kpi_report.round(2)
    print("✅ KPIs successfully calculated.")

    # 4. Export to Excel with a timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
    export_filename = f"Executive_KPI_Report_{timestamp}.xlsx"
    
    kpi_report.to_excel(export_filename, index=False)
    print(f"🎉 Pipeline Complete! Report saved as: {export_filename}")

if __name__ == "__main__":
    run_data_pipeline()