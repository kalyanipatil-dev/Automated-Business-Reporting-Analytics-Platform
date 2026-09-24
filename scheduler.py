import schedule
import time
import pandas as pd
from reports import export_to_excel, export_to_pdf

def daily_report_job():
    print("Running daily report job...")

    # Example dummy data (replace with real data source later)
    df = pd.DataFrame({
        "Sales": [100, 200, 150],
        "Profit": [20, 40, 30],
        "Expenses": [10, 15, 12]
    })

    # Generate Excel report
    excel_file = export_to_excel(df, "daily_report.xlsx")
    print(f"Excel report generated: {excel_file}")

    # Generate PDF report
    pdf_file = export_to_pdf(df, "daily_report.pdf")
    print(f"PDF report generated: {pdf_file}")

    print("Daily report job completed!")


def start_scheduler():
    schedule.every().day.at("09:00").do(daily_report_job)

    print("Scheduler started... Waiting for jobs...")

    while True:
        schedule.run_pending()
        time.sleep(1)
