import pandas as pd

def load_csv(file):
    """Load CSV file into a pandas DataFrame."""
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        print("Error loading CSV:", e)
        return None

def clean_data(df):
    """Basic cleaning: remove duplicates and handle missing values."""
    df = df.drop_duplicates()
    df = df.fillna(0)
    return df

def get_summary(df):
    """Return basic statistical summary."""
    return df.describe()
