# import  library
import streamlit as st 
# in terminal => streamlit run  {fileName}.py 
# CRT + C => cancel run server
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# 6 Form Element
st.title("Streamlit Form Demo")

# Form to hold the interactive element
with st.form(key="sample_form"):
    
    # Text Input
    st.subheader('Text Input')
    name = st.text_input('Enter your name')
    feedback = st.text_area('Provide your feedback')

    # Date and Time Input
    st.subheader('Date and Time Inputs')
    dob = st.date_input('Select your date of birth')
    time = st.time_input('Choose a preferred time')

    # Selectors
    st.subheader('Selectors')
    choice = st.radio('Choose an option', ['option1', 'option2', 'option3'])
    gender = st.selectbox('Select your gender', ['Male', 'Female', 'Other'])
    slider_value = st.select_slider("Select a range", options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Toggles and Checkboxes
    st.subheader('Toggles & Checkboxes')
    notifications = st.checkbox('Receive notifications?')
    toggles_value = st.checkbox('Enable dark mode', value=False)

    #Submit Button for the form
    submit_button = st.form_submit_button(label="Submit")



