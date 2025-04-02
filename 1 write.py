# 1 Install Streamlit :: in terminal => pip install streamlit

# import  library
import streamlit as st 
# in terminal => streamlit run  {fileName}.py 
# CRT + C => cancel run server

# 2 ST.write and Magic
st.write("Hello Streamlit for beginner to create web")
st.write("Hello world 1234")
st.write("How are you")

# Magic :: St.write() :: This is function is used to add anything to a Web app

st.write({"key": "value"}) 
st.write(True)
st.write(123)

# Anytime something must updated op the screen, Streamlit reruns your entire script from top to bottom
