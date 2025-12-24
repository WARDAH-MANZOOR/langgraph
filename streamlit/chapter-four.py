import streamlit as st
import pandas as pd
st.title("Chai Sales Dashboard")
file = st.file_uploader("Upload your sales data (CSV)", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.subheader("Sales Data Preview:")
    st.dataframe(df)
if file:
    st.subheader("Summary Stats")
    st.write(df.describe())
if file:
    cities = df["city"].unique()
    selected_city = st.selectbox("Select City to filter sales data", cities)
    filtered_data = df[df["city"] == selected_city]
    st.dataframe(filtered_data)