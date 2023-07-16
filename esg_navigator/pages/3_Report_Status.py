import streamlit as st
from streamlit_chat import message
import datetime
import numpy as np
import secrets
import pandas as pd
import os
from esg_navigator.backend.helper import chat_to_csv,load_chat_history, add_logo, on_input_change, load_complaints_db, write_to_complaints_db, displayPDF




st.set_page_config(
    page_title="Report Status",
    page_icon="👋",
    layout="wide"
)
add_logo() 
st.title("Report Status")

st.sidebar.markdown('''
        ---
        Created with ❤️ by UComply.
        ''')


if "valid_case" not in st.session_state:
     st.session_state['valid_case'] = False
if "process_id" not in st.session_state:
     st.session_state['process_id'] = ""


     

if not st.session_state['valid_case']:
    text_input = st.empty()
    button_check_process = st.empty()
    st.session_state['process_id'] = text_input.text_input("Please enter your case ID to see the status of your report")
    if button_check_process.button("Check Status"):
        st.session_state.valid_case = True    
        del text_input
        del button_check_process
        st.write("Success!")
        st.experimental_rerun()
else:

    load_complaints_db()
    complaints_df = st.session_state['complaints_db']

    st.write("Your current case ID is: ", st.session_state['process_id'])
    st.write("")

    status_value = complaints_df.loc[complaints_df['ID'] == st.session_state['process_id'], 'Status'].values[0]
    complaint_handler = complaints_df.loc[complaints_df['ID'] == st.session_state['process_id'], 'assigned_responsible'].values[0]


    c1, c2,c3 = st.columns((3,5,3), gap = "small")
    with c1:
        st.markdown('### Information on your case')
        st.write("**Your report status is:**", status_value)
        st.write("")
        st.write("**Your case is being handled by:**", complaint_handler)
    with c2:
        st.markdown('### Your submitted documents:')
        st.write("View your submitted Documents")
        if st.button("View my Documents",key = "View_button"):
            parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            pdf_path = os.path.join(parent_directory, 'data','pdfs', str(st.session_state['process_id'])+'.pdf')
            displayPDF(pdf_path)
    with c3:
        st.write("")
        st.write("Add new document")
        st.write("")
        if st.button("Submit new Documents", key = "Submit_button"):
            st.success("Documents uploaded successfully!")


    st.divider()

    st.header("Chat with your case manager")

    st.write("The section below serves as an anonymous chat functionality between you and your case manager.")
    load_chat_history(st.session_state['process_id'])

    if 'chat_history' not in st.session_state:
            st.session_state['chat_history'] = []
    if "user_input" not in st.session_state:
        st.session_state['user_input'] = ""

    chat_placeholder = st.empty()

    with chat_placeholder.container():   
        for i in range(len(st.session_state['chat_history'])):  
            chat = st.session_state['chat_history'][i]        
            message(chat["message"], is_user= not chat["is_officer"], key=f"{i}_user")


    with st.container():
        st.session_state.user_input = st.text_input("User Input:")
        if st.button("Submit message"):
            on_input_change(st.session_state['process_id'], is_officer = False)
            st.experimental_rerun()











