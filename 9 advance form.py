# import  library
import streamlit as st 
# in terminal => streamlit run  {fileName}.py 
# CRT + C => cancel run server
from datetime import datetime

# 8 Advance Form Example
st.title("User Information Form")

min_date = datetime(1990,1, 1)
max_date = datetime.now()

with st.form(key='user_info_form', clear_on_submit=True):
    name1 = st.text_input("Enter your name: ")
    birth_date = st.date_input("Enter your birthday", max_value=max_date, min_value=min_date)

    if birth_date:
        age = max_date.year - birth_date.year
        if birth_date.month > max_date.month or (birth_date.month == max_date.month and birth_date.day > max_date.day):
            age -= 1
        st.write(f'Your calculated age is {age} years')


    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        if not name1 or not birth_date:
            st.warning("Please fill in all of the fields")
        else:
            st.success(f"Thank your {name1}. YOur age is {age}.")
            st.balloons()

    