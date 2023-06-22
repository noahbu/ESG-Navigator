import streamlit as st
import pandas as pd
import numpy as np
import streamlit_authenticator as stauth

# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
#     )

# if st.session_state["authentication_status"]:
    
#     st.success("Logged in as: {}!".format(st.session_state["name"]))
#     #st.info("You can now access the app.")
#     authenticator.logout("Logout", "sidebar")
#     st.sidebar.title("Ucomply - Your Social Copilot")
#     st.sidebar.write("Welcome {}!".format(st.session_state["username"]))

st.title('ESG Manager View')

st.write(f"Welcome {st.session_state['username']}!")
st.write(f"Logged in as: {st.session_state['name']}!")
st.session_state["authenticator"].logout("Logout", "sidebar")

# Create a text input field
user_input = st.text_input("please enter here")

# Display the input value
st.write("You entered:", user_input)


# Create a question with a dropdown menu
selected_option = st.selectbox("Select an option", ["Sexual Harrassment", "Misconduct", "Discrimination"])

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

