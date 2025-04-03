# import  library
import streamlit as st 
# in terminal => streamlit run  {fileName}.py 
# CRT + C => cancel run server

# 10 Callbacks
if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}

def go_to_step2(name):
    st.session_state.info['name'] = name
    st.session_state.step = 2

def go_to_step1():
    st.session_state.step =1
    

if st.session_state.step == 1:
    st.header("Part 1: Info")
    name = st.text_input("Name", value= st.session_state.info.get("name", ""))
    
    # Callback function
    st.button("Next", on_click=go_to_step2, args=(name,))
    

if st.session_state.step ==2:
    st.header("Part 2: Review")
    
    st.subheader("Please review this")
    st.write(f"**Name**: {st.session_state.info.get('Name','')}")
    
    if(st.button("Submit")):
        st.success("Great!")
        st.balloons()
        st.session_state.info = {}
    
    # Callback function
    st.button("Back", on_click=go_to_step1)

#Callback :: Run before any other code on the next return