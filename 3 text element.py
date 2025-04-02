# import  library
import streamlit as st 
# in terminal => streamlit run  {fileName}.py 
# CRT + C => cancel run server

# 4 Text elements
st.title("Super Simple Title")
st.header("This is a header")
st.subheader("Subheader")
st.markdown("This is **Markdown**")
st.caption("small text")

code_example = """
def greet(name):
    print('hello', name)
"""

st.code(code_example, language="python")

st.divider() # line

