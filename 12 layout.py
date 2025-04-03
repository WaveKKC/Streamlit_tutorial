# import  library
import streamlit as st 
# in terminal => streamlit run  {fileName}.py 
# CRT + C => cancel run server

#11 Layouts

# Sidebar layout
st.sidebar.title("This is this Sidebar")
st.sidebar.write("You can place elements like sliders, button, and text here.")
sidebar_input = st.sidebar.text_input("Enter something in the sidebar")

#Tabs Layout
tab1, tab2, tab3 = st.tabs(['Tab1', 'Tab2', 'Tab3'])

with tab1:
    st.write('You are in Tab 1')

with tab2:
    st.write('You are in Tab 2')

with tab3:
    st.write('You are in Tab 3')

# Columns layout
col1, col2 = st.columns(2)
with col1:
    st.header("column 1")
    st.write("Content fo column 1")

with col2:
    st.header("column 2")
    st.write("Content fo column 2")

# Container example
with st.container(border=True):
    st.write('This is inside a container.')
    st.write('You can think of containers as a grouping for element.')
    st.write('Container help manage sections of the page')

# Empty placeholder
placeholder = st.empty()
placeholder.write("This is an empty placeholder, useful dynamic content.")

#Expander
with st.expander('Expand for more detail'):
    st.write('This is additional information that is hidden by default.')
    st.write('You can use expanders to keep you interface cleaner.')

#Popover (Tooltip)
st.write('Hover over this button for a tooltip')
st.button("Button with Tooltip", help="This is a tooltip or popover on hover.")

#Sidebar input handing
if sidebar_input:
    st.write(f'You entered in the sidebar: {sidebar_input}')



