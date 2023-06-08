import streamlit as st
import numpy as np



# Create a text input field
user_input = st.text_input("")

# Display the input value
st.write("You entered:", user_input)


# Create a question with a dropdown menu
selected_option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])

# Display the selected option
st.write("You selected:", selected_option)


# Create an upload field for PDF files
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

# Check if a file was uploaded
if uploaded_file is not None:
    # Process the uploaded file
    # For example, you can save it or read its contents
    st.write("File uploaded:", uploaded_file.name)
    pdf_contents = uploaded_file.read()
    st.write("PDF contents:", pdf_contents)
