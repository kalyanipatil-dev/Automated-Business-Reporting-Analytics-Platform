import pandas as pd

def calculate_kpis(df):
    """Return clean, user-friendly KPIs for GST business reporting."""
    kpis = {}

    # Total records (invoices)
    kpis["Total Records"] = int(len(df))

    # Total Sales (Total_Invoice)
    kpis["Total Sales"] = float(df["Total_Invoice"].sum())

    # Total Tax (CGST + SGST + IGST)
    kpis["Total Tax Collected"] = float(
        df["CGST"].sum() + df["SGST"].sum() + df["IGST"].sum()
    )

    # Average Invoice Value
    kpis["Average Invoice Value"] = float(df["Total_Invoice"].mean())

    # Highest Invoice
    kpis["Highest Invoice"] = float(df["Total_Invoice"].max())

    # Lowest Invoice
    kpis["Lowest Invoice"] = float(df["Total_Invoice"].min())

    return kpis


def generate_monthly_summary(df, date_column="Invoice_Date"):
    """Generate monthly summary for GST dataset."""

    if date_column not in df.columns:
        return None

    # Convert Invoice_Date safely
    df[date_column] = pd.to_datetime(df[date_column], errors="coerce")

    # Extract month
    df["month"] = df[date_column].dt.to_period("M").astype(str)

    # Create Sales column
    df["Sales"] = df["Total_Invoice"]

    # Create Tax column
    df["Tax"] = df["CGST"] + df["SGST"] + df["IGST"]

    # Group by month
    summary = df.groupby("month").agg({
        "Sales": "sum",
        "Tax": "sum",
        "Invoice_ID": "count"
    }).reset_index()

    summary.rename(columns={"Invoice_ID": "Invoice_Count"}, inplace=True)

    return summary
