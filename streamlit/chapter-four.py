import streamlit as st
import pandas as pd
st.title("Chai Sales Dashboard")
file = st.file_uploader("Upload your sales data (CSV)", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.subheader("Sales Data Preview:")
    st.dataframe(df)
    