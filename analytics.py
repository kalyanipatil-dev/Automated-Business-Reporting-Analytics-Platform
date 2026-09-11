import pandas as pd

def calculate_kpis(df):
    """Return basic KPIs for business reporting."""
    kpis = {}

    # Total rows
    kpis["total_records"] = len(df)

    # Numeric column summaries
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        kpis[f"{col}_sum"] = df[col].sum()
        kpis[f"{col}_avg"] = df[col].mean()
        kpis[f"{col}_max"] = df[col].max()
        kpis[f"{col}_min"] = df[col].min()

    return kpis


def generate_monthly_summary(df, date_column):
    """Generate monthly summary based on a date column."""
    df[date_column] = pd.to_datetime(df[date_column], errors="coerce")
    df["month"] = df[date_column].dt.to_period("M")

    summary = df.groupby("month").sum(numeric_only=True)
    return summary
