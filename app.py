import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Business Reporting & Analytics", layout="wide")

st.title("📊 Automated Business Reporting & Analytics Platform")

uploaded_file = st.file_uploader("Upload your business data (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # 1. Preview
    st.subheader("Preview of Uploaded Data")
    st.dataframe(df)

    # 2. Summary
    st.subheader("Basic Summary")
    st.write(df.describe())

    # ⭐ 3. Monthly Sales Trend
    st.subheader("Monthly Sales Trend")
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
    fig1 = px.line(monthly_sales, x='Month', y='Sales', title='Monthly Sales Trend')
    st.plotly_chart(fig1)

    # ⭐ 4. Region-wise Sales
    st.subheader("Region-wise Sales")
    region_sales = df.groupby('Region')['Sales'].sum().reset_index()
    fig2 = px.bar(region_sales, x='Region', y='Sales', title='Sales by Region', color='Region')
    st.plotly_chart(fig2)

    # ⭐ 5. Profit vs Expenses
    st.subheader("Profit vs Expenses")
    profit_expenses = df[['Date', 'Profit', 'Expenses']]
    profit_expenses['Date'] = pd.to_datetime(profit_expenses['Date'])
    fig3 = px.line(profit_expenses, x='Date', y=['Profit', 'Expenses'], title='Profit vs Expenses Over Time')
    st.plotly_chart(fig3)
