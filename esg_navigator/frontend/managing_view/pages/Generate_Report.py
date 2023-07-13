import streamlit as st
import pandas as pd
import numpy as np
import streamlit_authenticator as stauth
import datetime
import secrets



if st.session_state["authentication_status"]:
    #st.info("You can now access the app.")
    with st.sidebar:
        st.session_state['authenticator'].logout("Logout", "sidebar")
        st.sidebar.title("Ucomply - Your Social Copilot")
        st.sidebar.write(f"Welcome {st.session_state['username']}!")
        

        st.title('ESG Manager View')


elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')



st.title("Create a Report")
st.write("Please use the filter to create a customizeable report. Once everything is selected, please press generate Report")

st.header("Filter")

with st.form("My Feedback", clear_on_submit=True): # clear_on_submit deletes every field, once the submit button is pressed

    st.session_state['report_id'] =  secrets.token_hex(8)  # 

    categories = st.radio("Which Categories shall be included in the Report?",
        ('All',
         'Sexual Harrasment',
        'Discrimination',
        'Money Laundering',
        'Theft/Fraud',
        'ESG-Violation',
        'Conflict of interest'
        ))
    
    categories = st.radio("Which regions shall be included?",
        ('All', 
        'Germany',
        'France',
        'Slovenia'
        ))
    
    st.write("Select Timeframe:")

    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    start_date = st.date_input('Start date', today)
    end_date = st.date_input('End date', tomorrow)
    if start_date < end_date:
        st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
    else:
        st.error('Error: End date must fall after start date.')
        

    submitted = st.form_submit_button("Generate Report")

if submitted:
    st.markdown("##### A report with the following name has been created: (Date + ID)")
    st.code("R-" + str(start_date) + "-" + str(end_date) + st.session_state.report_id)
    st.markdown("##### The Report is safed at the specified location:")
    st.code("user/noah/documents/ucomply/reports")

