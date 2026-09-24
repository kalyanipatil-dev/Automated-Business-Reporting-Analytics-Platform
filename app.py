import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF

st.set_page_config(page_title="Business Reporting & Analytics", layout="wide")

st.title("📊 Automated Business Reporting & Analytics Platform")

uploaded_file = st.file_uploader("Upload your business data (CSV)", type=["csv"])

# PDF generator function
def generate_pdf(df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Business Report Summary", ln=True)

    for col in df.columns:
        try:
            pdf.cell(200, 10, txt=f"{col}: {df[col].iloc[0]}", ln=True)
        except:
            pass

    pdf.output("report.pdf")


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
    # 3. MONTHLY SALES TREND
    # -----------------------------
    st.subheader("Monthly Sales Trend")

    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M').astype(str)

    monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

    fig1 = px.line(monthly_sales, x='Month', y='Sales', title='Monthly Sales Trend')
    st.plotly_chart(fig1)

    # -----------------------------
    # 4. REGION-WISE SALES
    # -----------------------------
    st.subheader("Region-wise Sales")

    region_sales = df.groupby('Region')['Sales'].sum().reset_index()

    fig2 = px.bar(region_sales, x='Region', y='Sales', title='Sales by Region', color='Region')
    st.plotly_chart(fig2)

    # -----------------------------
    # 5. PROFIT VS EXPENSES
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
    # 6. EXPORT OPTIONS
    # -----------------------------
    st.subheader("📁 Export Options")

    # CSV Export
    csv_data = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download CSV",
        data=csv_data,
        file_name="report.csv",
        mime="text/csv"
    )

    # Excel Export
    df.to_excel("temp.xlsx", index=False)
    with open("temp.xlsx", "rb") as f:
        st.download_button(
            label="📊 Download Excel",
            data=f,
            file_name="report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    # PDF Export
    generate_pdf(df)
    with open("report.pdf", "rb") as f:
        st.download_button(
            label="📄 Download PDF",
            data=f,
            file_name="report.pdf",
            mime="application/pdf"
        )
