import streamlit as st
import pandas as pd
import plotly.express as px

from analytics import calculate_kpis, generate_monthly_summary
from reports import export_to_excel, export_to_csv, export_to_pdf

st.set_page_config(page_title="Business Reporting & Analytics", layout="wide")

st.title("📊 Automated Business Reporting & Analytics Platform")

uploaded_file = st.file_uploader("Upload your business data (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # -----------------------------
    # 1. DATA PREVIEW
    # -----------------------------
    st.subheader("Preview of Uploaded Data")
    st.dataframe(df)

    # -----------------------------
    # 2. BASIC SUMMARY
    # -----------------------------
    st.subheader("Basic Summary")
    st.write(df.describe())

    # -----------------------------
    # 3. KPIs (from analytics.py)
    # -----------------------------
    st.subheader("Key Performance Indicators (KPIs)")
    kpis = calculate_kpis(df)
    st.write(kpis)

    # -----------------------------
    # 4. MONTHLY SUMMARY (from analytics.py)
    # -----------------------------
    st.subheader("Monthly Summary")
    monthly_summary = generate_monthly_summary(df)
    if monthly_summary is not None:
        st.dataframe(monthly_summary)

    # -----------------------------
    # 5. MONTHLY SALES TREND
    # -----------------------------
    st.subheader("Monthly Sales Trend")

    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M').astype(str)

    monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

    fig1 = px.line(monthly_sales, x='Month', y='Sales', title='Monthly Sales Trend')
    st.plotly_chart(fig1)

    # -----------------------------
    # 6. REGION-WISE SALES
    # -----------------------------
    st.subheader("Region-wise Sales")

    region_sales = df.groupby('Region')['Sales'].sum().reset_index()

    fig2 = px.bar(region_sales, x='Region', y='Sales', title='Sales by Region', color='Region')
    st.plotly_chart(fig2)

    # -----------------------------
    # 7. PROFIT VS EXPENSES
    # -----------------------------
    st.subheader("Profit vs Expenses")

    profit_expenses = df[['Date', 'Profit', 'Expenses']]
    profit_expenses['Date'] = pd.to_datetime(profit_expenses['Date'])

    fig3 = px.line(
        profit_expenses,
        x='Date',
        y=['Profit', 'Expenses'],
        title='Profit vs Expenses Over Time'
    )
    st.plotly_chart(fig3)

    # -----------------------------
    # 8. EXPORT OPTIONS (using reports.py)
    # -----------------------------
    st.subheader("📁 Export Options")

    # CSV Export
    csv_file = export_to_csv(df, "report.csv")
    if csv_file:
        with open(csv_file, "rb") as f:
            st.download_button(
                label="📥 Download CSV",
                data=f,
                file_name="report.csv",
                mime="text/csv"
            )

    # Excel Export
    excel_file = export_to_excel(df, "report.xlsx")
    if excel_file:
        with open(excel_file, "rb") as f:
            st.download_button(
                label="📊 Download Excel",
                data=f,
                file_name="report.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    # PDF Export
    pdf_file = export_to_pdf(df, "report.pdf")
    if pdf_file:
        with open(pdf_file, "rb") as f:
            st.download_button(
                label="📄 Download PDF",
                data=f,
                file_name="report.pdf",
                mime="application/pdf"
            )
