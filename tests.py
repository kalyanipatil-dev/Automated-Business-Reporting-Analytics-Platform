import pandas as pd
from database import load_csv, clean_data, get_summary
from analytics import calculate_kpis

def test_load_csv():
    df = load_csv("sample.csv")
    assert df is not None
    print("CSV load test passed")

def test_clean_data():
    df = pd.DataFrame({"A": [1, 1, None]})
    cleaned = clean_data(df)
    assert cleaned.isnull().sum().sum() == 0
    print("Data cleaning test passed")

def test_kpis():
    df = pd.DataFrame({"Sales": [100, 200, 300]})
    kpis = calculate_kpis(df)
    assert kpis["total_records"] == 3
    print("KPI test passed")

if __name__ == "__main__":
    print("Running tests...")
    test_load_csv()
    test_clean_data()
    test_kpis()
    print("All tests passed!")
