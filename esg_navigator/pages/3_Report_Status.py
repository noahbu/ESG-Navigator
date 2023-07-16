import streamlit as st
from streamlit_chat import message
import datetime
import numpy as np
import secrets
import pandas as pd
import os
from esg_navigator.backend.helper import chat_to_csv,load_chat_history, add_logo, on_input_change



st.set_page_config(
    page_title="Report Status",
    page_icon="👋",
    layout="wide"
)
add_logo() 
st.title("Report Status")


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

    st.header("Chat with your case manager")

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










