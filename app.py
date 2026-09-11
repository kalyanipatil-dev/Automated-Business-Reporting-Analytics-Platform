import streamlit as st
import pandas as pd

st.set_page_config(page_title="Business Reporting & Analytics", layout="wide")

st.title("📊 Automated Business Reporting & Analytics Platform")

uploaded_file = st.file_uploader("Upload your business data (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview of Uploaded Data")
    st.dataframe(df)

    st.subheader("Basic Summary")
    st.write(df.describe())
