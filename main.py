import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from PIL import Image

st.set_page_config(page_title='MyHeritage - Data Profiling App', layout= "wide")
image = Image.open('./static/mh-logo.png')
# Web App Title

st.image(image)
st.markdown('''
# **Content Publication Team EDA App**
''')

# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file")
    sep = st.text_input('Set delimiter', '|')

# Pandas Profiling Report
if uploaded_file is not None and sep is not None:
    @st.cache
    def load_csv(datatype):
        csv = pd.read_table(uploaded_file,sep = sep, on_bad_lines='warn', encoding='utf-8', dtype=datatype)
        return csv
    df1 = load_csv('str')
    df2 = load_csv(None)
    pr = ProfileReport(df2, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df1)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting fo file to be uploaded.')

