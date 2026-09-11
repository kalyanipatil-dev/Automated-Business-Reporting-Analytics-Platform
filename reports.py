import pandas as pd

def export_to_excel(df, filename="report.xlsx"):
    """Export DataFrame to Excel file."""
    try:
        df.to_excel(filename, index=False)
        return True
    except Exception as e:
        print("Excel export error:", e)
        return False


def export_to_csv(df, filename="report.csv"):
    """Export DataFrame to CSV file."""
    try:
        df.to_csv(filename, index=False)
        return True
    except Exception as e:
        print("CSV export error:", e)
        return False


def export_to_html(df, filename="report.html"):
    """Export DataFrame to HTML file."""
    try:
        df.to_html(filename, index=False)
        return True
    except Exception as e:
        print("HTML export error:", e)
        return False
