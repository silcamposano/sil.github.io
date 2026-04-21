import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Load Local Excel File")

uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("DataFrame:")
    st.dataframe(df)

    if st.checkbox("Show Summary Statistics"):
        st.write("Summary Statistics:")
        st.write(df.describe())

    if st.checkbox("Show Correlation Heatmap"):
        st.write("Correlation Heatmap:")
        fig = px.imshow(df.corr(), text_auto=True, aspect="auto")
        st.plotly_chart(fig)    