# import  library
import streamlit as st 
# in terminal => streamlit run  {fileName}.py 
# CRT + C => cancel run server

#12 Advance widget concept
######################################################
# if "silder" not in st.session_state:
#     st.session_state.slider = 25

# min_value = st.slider("set min value", 0,50,25)
# slider_value = st.slider("slider", min_value, 100, st.session_state.slider)

######################################################
if "checkbox" not in st.session_state:
    st.session_state.checkbox = False

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox

st.checkbox("Show Input Field", value=st.session_state.checkbox, on_change=toggle_input)

if st.session_state.checkbox:
    user_input = st.text_input("Enter something")
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get("user_input", "")

st.write(f"User Input : {user_input}")