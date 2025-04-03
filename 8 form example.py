# import  library
import streamlit as st 
# in terminal => streamlit run  {fileName}.py 
# CRT + C => cancel run server
from datetime import datetime

# 7 Simple Form Example
st.title("User Information Form")

form_value = {
    "name": None,
    "height" : None,
    "gender": None,
    "dob": None,
}
min_date = datetime(1990,1, 1)
max_date = datetime.now()

with st.form(key='user_info_form'):
    form_value['name'] = st.text_input("Enter your name: ")
    form_value['height'] = st.number_input("Enter your height (com): ")
    form_value['gender'] = st.selectbox("Gender", ['Male', 'Female'])
    form_value['dob'] = st.date_input("Enter your birthday", max_value=max_date, min_value=min_date)


    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        if not all(form_value.values()):
            st.warning("Please fill in all of the fields")
        else:
            st.balloons()
            st.write("### Info")
            for (key, value) in form_value.items():
                st.write(f"{key} : {value}")

    