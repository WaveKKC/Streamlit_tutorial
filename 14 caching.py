# import  library
import streamlit as st 
# in terminal => streamlit run  {fileName}.py 
# CRT + C => cancel run server

# import time
#13 Caching
###############################################
# @st.cache_data(ttl=60) # Cache this data for 60 seconds
# def fetch_data():
#     # Simulate a slow data-fetching process
#     time.sleep(3) # Delays to mimic an API call
#     return {"data": "THis is cached data"}

# st.write("Fetching data....")
# data = fetch_data()
# st.write(data)

###############################################
file_path = "example.txt"

@st.cache_resource
def get_file_handle():
    # OPen the file in append mode, which create the file if it doesn't exit
    file = open(file_path, "a+")
    return file

# Use the cached file handler
file_handler = get_file_handle()

# Write to the file using the cache handler
if st.button("Write to File"):
    file_handler.write("New lone of text\n")
    file_handler.flush() #Ensure the content is written immediately
    st.success("Wrote a new line to the file!")

# Read and display the file contents
if st.button("Read File"):
    file_handler.seek(0)
    content = file_handler.read()
    st.text(content)

# Alway make sure to close the file when done (useful for resource cleanup)
st.button("Close File", on_click = file_handler.close)