import streamlit as st
import numpy as np
import secrets
import pandas as pd
from datetime import datetime
from esg_navigator.backend.helper import add_logo
import os
#from PyPDF2 import PdfFileReader, PdfWriter
import PyPDF2


# Get the root directory of the project (the location of the script)
st.set_page_config(
    page_title="File your report",
    page_icon="👋",
    layout="wide"
)
add_logo()

#set parent directory
parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def save_form(pdf_contents):
    print("Saving form...")
    parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(parent_directory, 'data', 'complaints_db.csv')
    st.session_state['complaints_db'] = pd.read_csv(file_path,sep= ";")
    #SAVE_PDF
    pdf_path = os.path.join(parent_directory, 'data','pdfs', str(id)+'.pdf')
    with open(pdf_path, 'wb') as out:
        out.write(pdf_contents)

    new_row = {'Timestamp':datetime.now(), 
               'ID':id, 
               'Urgency': select_urgency, 
               'Anonymity': selected_anonymity, 
               'Email': email, 
               'Category': choose_category,
               'Location': location,
               'Issue': description, 
               'Evidence': pdf_path, 
               'Status': 'Open'}
    
    # Append the row        
    st.session_state.complaints_db = pd.concat([st.session_state.complaints_db, pd.DataFrame([new_row])], ignore_index=True)

    st.session_state.complaints_db.to_csv(file_path,sep= ";", index=False)

    st.success("Successfully submitted your request - A colleague is going to take care of it")


def show_submission_details(submission_id, selected_anonymity):
    # Retrieve the submission details from the complaints database
    submission = st.session_state.complaints_db.loc[st.session_state.complaints_db['ID'] == submission_id]

    # Display the submission details
    st.header(f"Case - ID: {submission_id}")
    st.write("Please write down your Case - ID and store it safely. You need it to check on the status of your case and get in contact.")
    #st.write("Anonymity:", submission['Anonymity'].values[0])
    if selected_anonymity == "Email":
        st.write("Email:", submission['Email'].values[0])
    #st.write("Issue:", submission['Issue'].values[0])
    st.write("Status:", submission['Status'].values[0])




st.title('Filing a Complaint')

st.write("""
In this section you can file a complaint about any violations. 
You can do this either anonymous or you provide contact details, which allows us easier followup questions. Even if you share your contact details with us, they will only be forwarded to your company, if you actively agree. 
To provide the option to get in contact with You for understanding, missing info etc. 
you will be given a case_ID, which you should write down. With this you can see the status of the complaint and can also see questions beeing raised. 
In case you want to get in contact via email, please provide it. Then you will receive questions regarding your case directly and dont have to check online.
In case you have concern wether this is the right way to communicate your concerns, please file the complaint, as we will review it and will let you know about its eligibility. 
""")
         
# Create a question with a dropdown menu
selected_anonymity = st.selectbox("Select a contact option", ["Anonymous", "Email"])
email = None
pdf_contents = None
id = secrets.token_hex(8)  # Generates 16-character long hexadecimal

if selected_anonymity == "Anonymous":
    st.write(f"Process ID: {id}")

if selected_anonymity == "Email":
    email = st.text_input("Enter your email")

    # Create a second text input field to confirm email
    confirm_email = st.text_input("Confirm your email")

    # Compare the two emails and display a message
    if email and confirm_email:
        if email == confirm_email:
            st.success("The emails match.")
        else:
            st.error("The emails do not match. Please check and try again.")

#Urgency of the case
select_urgency = st.selectbox("How urgent is you case?", ["Look at it this week", "Urgent, please handle this today ",  "Super urgent, please handle this now"])

if select_urgency == "Super urgent, please handle this now":
    st.write("If you need immediate help, please call this number: +49 1234 56789. Otherwise we will directly get to work on your complaint")

#general category of the case
choose_category = st.selectbox("In which category does this case fit best?", [
    "Misconduct",
    "Sexual Harrasment",
    "Discrimination",
    "Money Laundering",
    "Theft/Fraud",
    "ESG-Violation",
    "Conflict of interest", 
    "Other"
])


#location of the case
location = st.text_area("Please describe where the Case takes place: at which specific team, which company is involved, in which location, etc.")


#general description
description = st.text_area("Please desccribe the Case") #text input field size is fixed to my knowledge, workaround with CSS oder Javascript exist. 
    

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



with col2:
    if st.button("Submit"):
        save_form(pdf_contents)
        show_submission_details(id, selected_anonymity)
        with col3:
            st.write("Micheal will handle you case")
            st.image(os.path.join(parent_directory, 'backend', 'trustworthy_hr_manager.jpg'), use_column_width=True)
            st.write("Michael Goodville is a proffesional conflict solver and will take the utmost care and sensitivity in handling your case")















