# import  library
import streamlit as st 
# in terminal => streamlit run  {fileName}.py 
# CRT + C => cancel run server
import pandas as pd

# 4 Data Element
st.title("Streamlit Element Demo")

# DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 32, 37, 45],
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Chef']
})

st.dataframe(df)

# Data Editor Section (Editable dataFrame)
st.subheader("Data Editor")
editable_df = st.data_editor(df)

# Static Table Section
st.subheader("Static Table")
st.table(df)

# Metrics Section
st.subheader('Metrics')
st.metric(label="Total Row", value=len(df))
st.metric(label="Average Age", value=round(df['Age'].mean(), 1))

# JSON and Dict Section
st.subheader("JSON and Dictionary")
sample_dict = {
    'name' : "Alice",
    'age' : 25,
    'skills' : ['Python', 'Data Science', 'Machine Learning']
}
st.json(sample_dict)

# Also show it as dictionary
st.write("Dictionary View: ", sample_dict)