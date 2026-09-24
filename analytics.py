import pandas as pd

def calculate_kpis(df):
    """Return clean, user-friendly KPIs for business reporting."""
    kpis = {}

    # Total records
    kpis["Total Records"] = int(len(df))

    # Numeric column summaries (clean output)
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        kpis[f"{col.capitalize()} Sum"] = int(df[col].sum())
        kpis[f"{col.capitalize()} Average"] = float(df[col].mean())
        kpis[f"{col.capitalize()} Max"] = int(df[col].max())
        kpis[f"{col.capitalize()} Min"] = int(df[col].min())

    return kpis


def generate_monthly_summary(df, date_column="Date"):
    """Generate monthly summary based on a date column."""
    if date_column not in df.columns:
        return None

    # Convert date column safely
    df[date_column] = pd.to_datetime(df[date_column], errors="coerce")

    # Extract month
    df["month"] = df[date_column].dt.to_period("M")

    # Group by month and sum numeric columns
    summary = df.groupby("month").sum(numeric_only=True)

    return summary.reset_index()
