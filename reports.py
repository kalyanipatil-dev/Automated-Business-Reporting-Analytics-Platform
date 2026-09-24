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
    """Export DataFrame to PDF file (GST optimized)."""
    try:
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=10)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="GST Business Report", ln=True)

        # Header row
        pdf.set_font("Arial", size=10, style="B")
        for col in df.columns:
            pdf.cell(40, 10, txt=str(col), border=1)
        pdf.ln()

        # Data rows
        pdf.set_font("Arial", size=8)
        for _, row in df.iterrows():
            for col in df.columns:
                pdf.cell(40, 10, txt=str(row[col]), border=1)
            pdf.ln()

        pdf.output(filename)
        return filename

    except Exception as e:
        print("PDF export error:", e)
        return None
