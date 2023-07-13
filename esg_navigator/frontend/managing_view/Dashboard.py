import streamlit as st
import streamlit_authenticator as stauth
import pickle
from pathlib import Path
import pandas as pd
import os
from streamlit_option_menu import option_menu
import yaml
from yaml.loader import SafeLoader 
from esg_navigator.backend.helper import app_init,load_css, load_complaints_db, load_manager_data
import datetime
import plost
from PIL import Image


st.set_page_config(
    page_title=" Welcome to Ucomply - Your Social Copilot",
    page_icon="👋",
    layout="centered"
)

#Only for effective dev: 

image = Image.open('../../design/logo/ucomply_Logo.png')
st.image(image)

#Variable initialization
app_init()

#Only display text if loggeed in:
if st.session_state["authentication_status"]:

    st.title("Integrity Intelligence Dashboard")
    st.write("")

    #Display login button
    st.session_state['authenticator'].logout("Logout", "sidebar")

    #Read maanager_database:
    load_manager_data()
    db = st.session_state['manager_db']


    #cCustomize sidebar
    with st.sidebar:
        
        st.title("Ucomply - Your Social Copilot")
        st.write(f"Welcome {st.session_state['username']}!")
    
        # st.sidebar.subheader('TBD inserting plot by region')
        # time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 

        # st.sidebar.subheader('Donut chart parameter')
        # donut_theta = st.sidebar.selectbox('Select quarter', ('q2', 'q3'))

        # st.sidebar.subheader('Line chart parameters')

        # plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
        # plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

        st.sidebar.markdown('''
        ---
        Created with ❤️ by UComply.
        ''')


    #Dashboard Build: ROW 1
    col1, col2, col3 = st.columns(3)
    col1.metric("New open cases", "1", "100%")
    col2.metric("This months complaints", " 3", "33%")
    col3.metric("Complaints Location: EMEA ", "10", "10%")

    #Dashboard Build: ROW 2
    #To be altered to display the correct data
    df_status = db.groupby('Status').size().reset_index(name='Occurrences')
    
    encoding = {
        "field": "Status", 
        "type": "nominal",
        "scale": {
            "domain": ["Closed", "Pending", "New"],
            "range": ["#155D59", "#0C6D69", "#FFCB43"]
        }}
    

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
        st.markdown('### Cases by Status')
        plost.donut_chart(
            data=df_status,
            theta = "Occurrences",
            color = encoding,
            height = 350,

            legend='bottom', 
            use_container_width=True)

    # Row C
    #Create new db for bar chart where we do groupby Category and sum up its Occurrences: 
    df_bar = db.groupby('Category').size().reset_index(name='Occurrences')

    st.markdown('### Cases by classification')
    plost.bar_chart(
        data=df_bar,
        bar = 'Category',
        value='Occurrences',
        color = "#155D59",
        use_container_width=True)

    
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')




  