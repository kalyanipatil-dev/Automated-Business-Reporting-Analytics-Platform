import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st

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

    for key, value in kpis.items():
        st.write(f"**{key}:** {value}")

    # -----------------------------
    # 4. MONTHLY SUMMARY (from analytics.py)
    # -----------------------------
    st.subheader("Monthly Summary")
    monthly_summary = generate_monthly_summary(df)
    if monthly_summary is not None:
        st.dataframe(monthly_summary)

    # -----------------------------
    # 5. MONTHLY SALES TREND (GST FIX)
    # -----------------------------
    st.subheader("Monthly Sales Trend")

    # Convert Invoice_Date
    df['Invoice_Date'] = pd.to_datetime(df['Invoice_Date'])

    # Create Month column
    df['Month'] = df['Invoice_Date'].dt.to_period('M').astype(str)

    # Use Total_Invoice as Sales
    df['Sales'] = df['Total_Invoice']

    # Group by Month
    monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

    fig1 = px.line(monthly_sales, x='Month', y='Sales', title='Monthly Sales Trend')
    st.plotly_chart(fig1)

    # -----------------------------
    # 6. REGION-WISE SALES (GST FIX)
    # -----------------------------
    st.subheader("Region-wise Sales")

    region_sales = df.groupby('Place_of_Supply')['Sales'].sum().reset_index()

    fig2 = px.bar(region_sales, x='Place_of_Supply', y='Sales',
                  title='Sales by Region', color='Place_of_Supply')
    st.plotly_chart(fig2)

    # -----------------------------
    # 7. EXPORT OPTIONS
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

# Premium Graphical Analytics Background
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1627556704304-1d6f5a8a7c2f"); /* Futuristic analytics theme */
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

[data-testid="stSidebar"] {
background: rgba(15,15,15,0.9);
}

.block-container {
background: rgba(20,20,20,0.7);
border-radius: 12px;
padding: 20px;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
