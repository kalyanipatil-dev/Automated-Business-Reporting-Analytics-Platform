import pandas as pd
from fpdf import FPDF

def export_to_excel(df, filename="report.xlsx"):
    """Export DataFrame to Excel file."""
    try:
        df.to_excel(filename, index=False)
        return filename
    except Exception as e:
        print("Excel export error:", e)
        return None


def export_to_csv(df, filename="report.csv"):
    """Export DataFrame to CSV file."""
    try:
        df.to_csv(filename, index=False)
        return filename
    except Exception as e:
        print("CSV export error:", e)
        return None


def export_to_html(df, filename="report.html"):
    """Export DataFrame to HTML file."""
    try:
        df.to_html(filename, index=False)
        return filename
    except Exception as e:
        print("HTML export error:", e)
        return None


def export_to_pdf(df, filename="report.pdf"):
    """Export DataFrame to PDF file."""
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Business Report Summary", ln=True)

        for col in df.columns:
            try:
                pdf.cell(200, 10, txt=f"{col}: {df[col].iloc[0]}", ln=True)
            except:
                pass

        pdf.output(filename)
        return filename

    except Exception as e:
        print("PDF export error:", e)
        return None
