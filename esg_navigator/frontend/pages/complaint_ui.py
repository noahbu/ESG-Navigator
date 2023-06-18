import streamlit as st
import numpy as np
import secrets




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

if selected_option == "Anonymous":
    id = secrets.token_hex(8)  # Generates 16-character long hexadecimal
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
    st.write("PDF contents:", pdf_contents)



