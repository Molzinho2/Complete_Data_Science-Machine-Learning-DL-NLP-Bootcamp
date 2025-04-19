import pandas as pd
import streamlit as st

st.title("Streamlit Text Input")

name = st.text_input("Enter your name: ")

age = st.slider("Select your age:", 1, 100, 18)

st.write("Your age is", age)

option = ['Python', 'Java', 'C++', 'Javascript']
choice = st.selectbox('Choose your favorite linguage: ', option)
st.write("Your favorite language is", choice)

if name:
    st.write(f"Hello, {name}")

data ={
    "Name": ["John", "Doe", "Jane", "Jill"],
    "Age": [21, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)