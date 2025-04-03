# import  library
import streamlit as st 
# in terminal => streamlit run  {fileName}.py 
# CRT + C => cancel run server


# 9 Session state
# A simple counter variable, without session state
# counter = 0

# st.write(f"Counter value: {counter}")

# # Button to increment the counter
# if st.button("Increment Count"):
#     counter +=1
#     st.write(f"Counter incremented to {counter}")
# else:
#     st.write(f"Count stays at {counter}")

####################################################3
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter"):
    st.session_state.counter +=1
    st.write(f'Counter Increment to {st.session_state.counter}')

if st.button("Reset"):
    st.session_state.counter = 0

st.write(f'Counter value: {st.session_state.counter}')

# Session state is something that we can use to store values within the same user session