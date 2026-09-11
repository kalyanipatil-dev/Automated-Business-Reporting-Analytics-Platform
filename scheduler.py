import schedule
import time
import pandas as pd
from reports import export_to_excel

def daily_report_job():
    print("Running daily report job...")

    # Example dummy data
    df = pd.DataFrame({
        "Sales": [100, 200, 150],
        "Profit": [20, 40, 30]
    })

    export_to_excel(df, "daily_report.xlsx")
    print("Daily report generated!")

def start_scheduler():
    schedule.every().day.at("09:00").do(daily_report_job)

    print("Scheduler started...")

    while True:
        schedule.run_pending()
        time.sleep(1)
