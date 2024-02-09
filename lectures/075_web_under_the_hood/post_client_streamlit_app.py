import requests
import streamlit as st

st.markdown("# Churn probability test")

st.markdown("#### Input parameters")

uc_grad = st.toggle("UC Graduate?")
age     = st.slider("Age", 18, 100)

response = requests.post(url=f"http://localhost:5000/get_churn_probability", json = {'gender':'male', 'age':age, 'uc_grad':uc_grad})
st.write(response.json())
