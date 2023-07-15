import streamlit as st
import pandas as pd
import numpy as np
import streamlit_authenticator as stauth
import datetime
import secrets
from esg_navigator.backend.helper import add_logo
 

st.set_page_config(
    page_title="Generate your Compliance Report",
    page_icon="👋",
    layout="centered"
)

#Load logo to the sidebar
add_logo()




# Load the login module
if st.session_state["authentication_status"]:
        #Write the title and the description
    st.title("Generate your Compliance Report")
    st.write("Please use the filter to create a customizeable report.")
    st.write("Once everything is selected, please press generate report")
    st.divider()
    #Customize sidebar
    with st.sidebar:
        st.session_state['authenticator'].logout("Logout", "sidebar")
        st.sidebar.title("Ucomply - Your Social Copilot")
        st.sidebar.write(f"Welcome {st.session_state['username']}!")
        st.markdown('''
        ---
        Created with ❤️ by UComply.
        ''')
        
    st.header("Customize your Report")
    #Create a form to filter the report
    with st.form("My Feedback", clear_on_submit=True): # clear_on_submit deletes every field, once the submit button is pressed

        #Generate a random report ID
        st.session_state['report_id'] =  secrets.token_hex(8)  # 
        #Filter the report by categories to be included
        categories = st.radio("Which Categories shall be included in the Report?",
            ('All',
            'Sexual Harrasment',
            'Discrimination',
            'Money Laundering',
            'Theft/Fraud',
            'ESG-Violation',
            'Conflict of interest'
            ))
        
        #Filter the report by regions to be included
        regions = st.radio("Which regions shall be included?",
            ('All', 
            'Germany',
            'France',
            'Slovenia'
            ))
        #Filter the report by time
        st.write("Select Timeframe:")
        # Get timestamps for today and tomorrow
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        start_date = st.date_input('Start date', today)
        end_date = st.date_input('End date', tomorrow)

        if start_date < end_date:
            st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
        else:
            st.error('Error: End date must fall after start date.')
            
        #Create a button to submit the form
        submitted = st.form_submit_button("Generate Report")

    #Display the report
    if submitted:
        st.markdown("##### A report with the following name has been created: (Date + ID)")
        st.code("R-" + str(start_date) + "-" + str(end_date) + st.session_state.report_id)
        st.markdown("##### The Report is safed at the specified location:")
        st.code("user/noah/documents/Ucomply/reports/"+ str(st.session_state['report_id']))



elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')





