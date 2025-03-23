import streamlit as st
import pandas as pd

st.set_page_config(page_title="Charge Calculator",page_icon="💰")
st.title("Insurace Charge Calculator")
data=pd.read_csv("insurance.csv")

#categorizing bmi
bmi_bins = [0, 18.5, 24.9, 29.9, float('inf')]
bmi_labels = ['Underweight', 'Fit', 'Overweight', 'Obese']
data['bmi_category'] = pd.cut(data['bmi'], bins=bmi_bins, labels=bmi_labels, right=True)

#categorizing age
age_bins = [18, 35, 50, float('inf')]
age_labels = ['Young Adult', 'Middle-aged', 'Senior']
data['age_category'] = pd.cut(data['age'], bins=age_bins, labels=age_labels, right=True)

st.subheader("Enter your details here: ")
#taking user details
age_category = st.selectbox("Select Age Category:", ['Young Adult', 'Middle-aged', 'Senior'])
bmi_category = st.selectbox("Select BMI Category:", ['Underweight', 'Fit', 'Overweight', 'Obese'])
sex = st.selectbox("Select Gender:", ['male', 'female'])
children = st.number_input("Number of Children:", min_value=0, max_value=10, step=1)
smoker = st.selectbox("Are you a Smoker?", ['no','yes'])
region = st.selectbox("Select Region:",["northeast","northwest","southeast","southwest"])

#filtering data according to user input
filtered_data = data[
    (data['age_category'] == age_category) &
    (data['bmi_category'] == bmi_category) &
    (data['sex'] == sex) &
    (data['children'] == children) &
    (data['smoker'] == smoker) &
    (data['region'] == region)
]

#calculating estimated insurance charge
if not filtered_data.empty:
    estimated_charge = filtered_data['charges'].mean()
    st.write(f"### Estimated Insurance Cost: **${estimated_charge:.2f}**")
else:
    st.write("### No exact matches found. Try changing your inputs.")