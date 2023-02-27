import streamlit as st
import pandas as pd
import os


st.set_page_config(
    page_title = "Home ",
    page_icon = ":heartbeat:"
)

st.title("Welcome to my web app :heartbeat:")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# st.text(FILE_DIR)

dir_of_interest = os.path.join(FILE_DIR,'iris.csv')
# st.text(dir_of_interest)

df = pd.read_csv(dir_of_interest)



# uploading file by user

st.header("Choose a CSV file")
uploaded_file = st.file_uploader("", accept_multiple_files= False, type = 'csv')

st.dataframe(df)


st.session_state.df = df 

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    st.subheader("Your uploaded Data :")
    st.write(df)
    st.session_state.df = df

 
