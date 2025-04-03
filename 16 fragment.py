# import  library
import streamlit as st 
# in terminal => streamlit run  {fileName}.py 
# CRT + C => cancel run server

# 15 Fragments
st.title("My Awesome App")

@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter text")
    

@st.fragment()
def filter_and_file():
    new_cols = st.columns(5)
    new_cols[0].checkbox('Filter')
    new_cols[1].file_uploader("upload image")
    new_cols[2].selectbox("Choose option", ['option1', 'option2', 'option3'])
    new_cols[3].slider('select value', 0, 100, 50)
    new_cols[4].text_input("Enter text")

toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("Select", [1,2,3], None)
cols[1].button("Upload")
filter_and_file()

#Fragments :: are a way to rerun only certain portions of your user interface and better organize or separate out your code