import streamlit as st
import numpy as np
import secrets
import pandas as pd
from datetime import datetime
import os
from PyPDF2 import PdfFileReader, PdfWriter



# Get the root directory of the project (the location of the script)


def save_form(pdf_contents):
    print("Saving form...")
    parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(parent_directory, 'data', 'complaints_db.csv')
    st.session_state['complaints_db'] = pd.read_csv(file_path,sep= ";")
    #SAVE_PDF
    pdf_path = os.path.join(parent_directory, 'data','pdfs', str(id)+'.pdf')
    with open(pdf_path, 'wb') as out:
        out.write(pdf_contents)

    new_row = {'Timestamp':datetime.now(), 'ID':id, 'Anonymity': selected_option, 'Email': email, 'Issue': user_text, 'Evidence': pdf_path, 'Status': 'Open'}
    
    # Append the row        
    st.session_state.complaints_db = pd.concat([st.session_state.complaints_db, pd.DataFrame([new_row])], ignore_index=True)

    st.session_state.complaints_db.to_csv(file_path,sep= ";", index=False)

    st.success("Successfully submitted your request - A colleague is going to take care of it")


st.title('Filing a Complaint')

st.write("""
In this section you can file a complaint about human rights violation anonoumously.
To provide the option to get in contact with You regarding the complaint in case of questions beeing raised for understanding, missing info etc. 
you will be given a case_ID, which you should write down. With this you can see the status of the complaint and can also see questions beeing raised. 
In case you want to get in contact via email, please provide it. Then you will receive questions regarding your case directly and dont have to check online.
In case you have concern wether this is the right way to communicate your concerns, please file the complaint, as we will review it and will let you know about its eligibility. 
""")
         
# Create a question with a dropdown menu
selected_option = st.selectbox("Select a contact option", ["Anonymous", "Email"])
email = None
pdf_contents = None
id = secrets.token_hex(8)  # Generates 16-character long hexadecimal

if selected_option == "Anonymous":
    st.write(f"Process ID: {id}")

if selected_option == "Email":
    email = st.text_input("Enter your email")

    # Create a second text input field to confirm email
    confirm_email = st.text_input("Confirm your email")

    # Compare the two emails and display a message
    if email and confirm_email:
        if email == confirm_email:
            st.success("The emails match.")
        else:
            st.error("The emails do not match. Please check and try again.")

user_text = st.text_area("Please desccribe your issue") #text input field size is fixed to my knowledge, workaround with CSS oder Javascript exist. 
    


# Create an upload field for PDF files
uploaded_file = st.file_uploader("Upload a PDF as case fo evidence to your complaint", type="pdf")

# Check if a file was uploaded
if uploaded_file is not None:
    # Process the uploaded file
    # For example, you can save it or read its contents
    st.write("File uploaded:", uploaded_file.name)
    pdf_contents = uploaded_file.read()
    #st.write("PDF contents:", pdf_contents)
    

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Submit"):
        save_form(pdf_contents)











