# import  library
import streamlit as st 
# in terminal => streamlit run  {fileName}.py 
# CRT + C => cancel run server

# 3 button
print('Run')
pressed = st.button("Press me") 
# return boolean type {True:False}
print('First: ', pressed)

pressed2 = st.button("Second Button")
print('Second: ', pressed2)

# Result
# 1 Run server app
# Run
# First False
# Second True

# 2 click first button
# -> page refresh
# Run
# First True
# Second False

# 3 click second button
# -> page refresh
# Run
# First True
# Second False