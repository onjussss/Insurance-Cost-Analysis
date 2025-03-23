import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset View",page_icon="💾")
st.title("Dataset View")    
data=pd.read_csv("insurance_dataset_analysis/insurance.csv")
st.write(data)
