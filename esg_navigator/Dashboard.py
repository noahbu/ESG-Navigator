import streamlit as st
import streamlit_authenticator as stauth
import pickle
from pathlib import Path
import pandas as pd
import os
from streamlit_option_menu import option_menu
import yaml
from yaml.loader import SafeLoader 
from backend.helper import app_init,load_css, load_complaints_db, load_manager_data
import datetime
import plost
from PIL import Image


st.set_page_config(
    page_title=" Welcome to Ucomply - Your Social Copilot",
    page_icon="👋",
    layout="centered"
)

#load logo section
image = Image.open('/app/ucomply/esg_navigator/design/logo/ucomply_Logo.png')
st.image(image)

#Variable initialization & login functionality
app_init()

#Only display text if loggeed in:
if st.session_state["authentication_status"]:
    #Write Title
    st.title("Integrity Intelligence Dashboard")
    st.write("")

    #Display logout button in the sidebar button
    st.session_state['authenticator'].logout("Logout", "sidebar")

    #Read filtered complaints_db according to your login:
    if 'manager_db' not in st.session_state:
        st.session_state['manager_db'] = None

    st.session_state['manager_db'] = load_manager_data()
    db = st.session_state['manager_db']
    st.write(db)

    #Customize sidebar
    with st.sidebar:
        
        #Display username in the sidebar
        st.title("Ucomply - Your Social Copilot")
        st.write(f"Welcome {st.session_state['username']}!")

        st.markdown('''
        ---
        Created with ❤️ by UComply.
        ''')


    #Dashboard Build: ROW 1
    col1, col2, col3 = st.columns(3)

    df_status = db.groupby('Status').size().reset_index(name='Occurrences')
    count_new = df_status[df_status['Status'] == 'New']['Occurrences']

    #Get percentage of new cases in percentage in comparison to 
    col1.metric("New open cases", count_new, "10%")


    # This months complaints 
    col2.metric("This months complaints", " 15", "33%")
    #Filter open complaints by region for Germany
 
    org_byregion = db.groupby('Region').size().reset_index(name='Occurrences')
    counts_byregion = org_byregion[org_byregion['Region'] == 'Germany']['Occurrences']
    col3.metric("Complaints Location: Germany ", counts_byregion, "10%")

    #Dashboard Build: ROW 2    

    c1, c2 = st.columns((5,5), gap = "large")
    with c1:
        st.markdown('### Cases by Location')
        df_region = db.groupby('Region').size().reset_index(name='Occurrences')
        plost.bar_chart(
        data=df_region,
        bar = 'Region',
        value='Occurrences',
        color = "#155D59",
        use_container_width=True,
        height = 350,
        direction='horizontal')

    with c2:
        #Display the Donut active status chart

        #Color encoding for the donut chart
        encoding = {
            "field": "Status", 
            "type": "nominal",
            "scale": {
                "domain": ["Closed", "Pending", "New"],
                "range": ["#155D59", "#0C6D69", "#FFCB43"]
            }}

        st.markdown('### Cases by Status')
        #Plot the donut chart
        plost.donut_chart(
            data=df_status,
            theta = "Occurrences",
            color = encoding,
            height = 350,
            legend='bottom', 
            use_container_width=True)

    #Dashboard Build: ROW 3
    #Create new db for bar chart where we do groupby Category and sum up its Occurrences: 
    df_bar = db.groupby('Category').size().reset_index(name='Occurrences')
    st.markdown('### Cases by Report Category')
    #Plot the bar chart
    plost.bar_chart(
        data=df_bar,
        bar = 'Category',
        value='Occurrences',
        color = "#155D59",
        use_container_width=True)

#Display error message if login is incorrect
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
#Display warning message if no login is entered
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')




  