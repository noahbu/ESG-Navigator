
import sys
import os
import streamlit as st
import numpy as np
import secrets
import pandas as pd
from datetime import datetime
from backend.helper import add_logo
import os
import PyPDF2


st.set_page_config(
    page_title="File your report",
    page_icon="👋",
    layout="wide"
)
add_logo()

#set parent directory
parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#save feedback
def save_feedback(pdf_contents):
    print("Saving form...")
    parent_directory = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    st.write(parent_directory)
    file_path = os.path.join(parent_directory, 'esg_navigator/data/complaints_db.csv')
    st.write(file_path)
    st.session_state['complaints_db'] = pd.read_csv(file_path,sep= ";")
    #SAVE_PDF
    if pdf_contents is not None:
        pdf_path = os.path.join(parent_directory, 'data','pdfs', str(id)+'.pdf')
        with open(pdf_path, 'wb') as out:
            out.write(pdf_contents)
    else:
        pdf_path = ""

    new_row = {'Timestamp':datetime.now(), 
               'ID':st.session_state.process_id, 
               'Anonymity': selected_anonymity, 
               'Email': email, 
               'Category': 'Feedback',
               'Location': location,
               'Issue': description, 
               'Evidence': pdf_path, 
               'Status': 'Open',
               'Manager': 'admin'}
    
    # Append the row        
    st.session_state.complaints_db = pd.concat([st.session_state.complaints_db, pd.DataFrame([new_row])], ignore_index=True)

    st.session_state.complaints_db.to_csv(file_path,sep= ";", index=False)

    st.success("Successfully submitted your Feedback - A colleague is going to forward it")



# save a complaint
def save_complaint(pdf_contents):
    print("Saving form...")
    parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(parent_directory, 'data', 'complaints_db.csv')
    st.session_state['complaints_db'] = pd.read_csv(file_path,sep= ";")
    #SAVE_PDF
    if pdf_contents is not None:
        pdf_path = os.path.join(parent_directory, 'data','pdfs', str(id)+'.pdf')
        with open(pdf_path, 'wb') as out:
            out.write(pdf_contents)
    else:
        pdf_path = ""

    new_row = {'Timestamp':datetime.now(), 
               'ID':st.session_state.process_id, 
               'Urgency': select_urgency, 
               'Anonymity': selected_anonymity, 
               'Email': email, 
               'Category': choose_category,
               'Location': location,
               'Issue': description, 
               'Evidence': pdf_path, 
               'Status': 'Open',
               'Manager': 'admin'}
    
    # Append the row        
    st.session_state.complaints_db = pd.concat([st.session_state.complaints_db, pd.DataFrame([new_row])], ignore_index=True)

    st.session_state.complaints_db.to_csv(file_path,sep= ";", index=False)

    st.success("Successfully submitted your request - A colleague is going to take care of it")



#shows submission details and summarizes them
def show_submission_details(submission_id, selected_anonymity):
    # Retrieve the submission details from the complaints database
    submission = st.session_state.complaints_db.loc[st.session_state.complaints_db['ID'] == submission_id]

    # Display the submission details
    st.title(f"Case - ID: {submission_id}")
    st.subheader("Please write down your Case - ID and store it safely. You need it to check on the status of your case and get in contact.")
    #st.write("Anonymity:", submission['Anonymity'].values[0])
    if selected_anonymity == "Email":
        st.write("Email:", submission['Email'].values[0])
    #st.write("Issue:", submission['Issue'].values[0])
    st.write("Status:", submission['Status'].values[0])


#############################################################################################################
#############################################################################################################
#                           Start of the Page                                                               #
#############################################################################################################
#############################################################################################################


#choosing between complaint or feedback

st.title("Would you like to give Feedback or file a Complaint?")

feedback_complaint = st.radio(
    "Please select Feedback or Complaint:",
    ('Feedback', 'Complaint'))


#############################################################################################################
#                           Giving Feedback                                                                 #
#############################################################################################################

if feedback_complaint == 'Feedback':
    st.header('Giving Feedback')

    st.write("""
    Hey, we really appreciate that You want to give Feedback, to increase your working experience!
    First of all: If you want to give Feedback to the people within your team and direct supervisors, it always encouraged to this directly and in person. Everyone is happy to hear, that the are doing something good ;)
    When you give Feedback, please highlight good topics and also topics that could be improved!

    Please also give some details on you position within the company, so we can forward the feedback to the corresponding person!
    """)


    # selection box has to be outside of st.form, as it has to reload
    selected_anonymity = st.selectbox("Select contact option", ["Anonymous", "Email"])

    #st.form creates a container, in which the code is only run once the submission button is pressed
    with st.form("My Feedback", clear_on_submit=True): # clear_on_submit deletes every field, once the submit button is pressed
        

        #zero initialize the variables
        email = None
        pdf_contents = None
        uploaded_file = None
        pdf_contents = None


        if 'process_id' not in st.session_state:
                st.session_state['process_id'] =  secrets.token_hex(8)  # 


        if selected_anonymity == "Anonymous":
            st.write("You will be provided with a Feedback-ID after submission. You can use this to anonymously answer questions regarding your feedback, to clarify specific points")

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

        #location of the case
        location = st.text_area("In which Team and at which location do you work?")


        #general description
        description = st.text_area("Please give your feedback here:") #text input field size is fixed to my knowledge, workaround with CSS oder Javascript exist. 

        # Create an upload field for PDF files
        uploaded_file = st.file_uploader("Upload a PDF in case you want to provide additional information", type="pdf")

        # Check if a file was uploaded
        if uploaded_file is not None:
            # Process the uploaded file
            # For example, you can save it or read its contents
            st.write("File uploaded:", uploaded_file.name)
            pdf_contents = uploaded_file.read()

            #st.write("PDF contents:", pdf_contents)

            

        col1, col2 = st.columns([3, 1], gap="large")

        submitted = st.form_submit_button("Submit")

    if submitted:
        save_feedback(pdf_contents)
        with col1: 
            show_submission_details(st.session_state.process_id, selected_anonymity)
            
        with col2: 
            st.image(os.path.join(parent_directory, 'backend', 'trustworthy_hr_manager.jpg'), use_column_width=True)
            st.header("Micheal will forward your feedback")
            st.write("Michael Goodville is a proffesional conflict solver and is always lookign forward to give positive Feedback")





#############################################################################################################
#                           Filing a Complaint                                                              #
#############################################################################################################


if feedback_complaint == 'Complaint':
    st.header('Filing a Case')

    st.write("""
    In this section you can file a complaint about any violations. 
    You can do this either anonymous or you provide contact details, which allows us easier followup questions. Even if you share your contact details with us, they will only be forwarded to your company, if you actively agree. 
    To provide the option to get in contact with You for understanding, missing info etc. 
    you will be given a case_ID, which you should write down. With this you can see the status of the complaint and can also see questions beeing raised. 
    In case you want to get in contact via email, please provide it. Then you will receive questions regarding your case directly and dont have to check online.
    In case you have concern wether this is the right way to communicate your concerns, please file the complaint, as we will review it and will let you know about its eligibility. 
    """)
    

    # selection box has to be outside of st.form, as it has to reload
    selected_anonymity = st.selectbox("Select contact option", ["Anonymous", "Email"])

    #st.form creates a container, in which the code is only run once the submission button is pressed
    with st.form("My Feedback", clear_on_submit=True): # clear_on_submit deletes every field, once the submit button is pressed

        email = None
        pdf_contents = None
        uploaded_file = None
        pdf_contents = None


        if 'process_id' not in st.session_state:
                st.session_state['process_id'] =  secrets.token_hex(8)  # 


        if selected_anonymity == "Anonymous":
            #st.caption(f"Process ID: {st.session_state.process_id}")
            st.write("You will be provided with a Case-ID after submission. You can use this to anonymously track status of the cases and get in contact with the case manager")

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
        location = st.text_area("Where did your incident happen at which specific team, which company is involved, in which location, etc.")


        #general description
        description = st.text_area("Please desribe what you observed") #text input field size is fixed to my knowledge, workaround with CSS oder Javascript exist. 

        # Create an upload field for PDF files
        uploaded_file = st.file_uploader("Upload a PDF as case fo evidence to your complaint", type="pdf")

        # Check if a file was uploaded
        if uploaded_file is not None:
            # Process the uploaded file
            # For example, you can save it or read its contents
            st.write("File uploaded:", uploaded_file.name)
            pdf_contents = uploaded_file.read()

            #st.write("PDF contents:", pdf_contents)

            

        col1, col2 = st.columns([3, 1], gap="large")

        submitted = st.form_submit_button("Submit")

    if submitted:
        save_complaint(pdf_contents)
        with col1: 
            show_submission_details(st.session_state.process_id, selected_anonymity)
            
        with col2: 
            st.image(os.path.join(parent_directory, 'esg_navigator/backend', 'trustworthy_hr_manager.jpg'), use_column_width=True)
            st.header("Micheal will handle you case")
            st.write("Michael Goodville is a proffesional conflict solver and will take the utmost care and sensitivity in handling your case")