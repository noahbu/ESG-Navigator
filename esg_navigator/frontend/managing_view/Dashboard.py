import streamlit as st
import streamlit_authenticator as stauth
import pickle
from pathlib import Path
import pandas as pd
import os
from streamlit_option_menu import option_menu
import yaml
from yaml.loader import SafeLoader 
from esg_navigator.backend.helper import app_init,load_css, load_complaints_db
import datetime
import plost
from PIL import Image


st.set_page_config(
    page_title=" Welcome to Ucomply - Your Social Copilot",
    page_icon="👋",
    layout="centered"
)

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

    #cCustomize sidebar
    with st.sidebar:
        
        st.title("Ucomply - Your Social Copilot")
        st.write(f"Welcome {st.session_state['username']}!")
    

        st.sidebar.subheader('TBD inserting plot by region')
        time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 

        st.sidebar.subheader('Donut chart parameter')
        donut_theta = st.sidebar.selectbox('Select quarter', ('q2', 'q3'))

        st.sidebar.subheader('Line chart parameters')

        plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
        plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

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
    seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
    cases = pd.DataFrame(dict(
        company=['Sexual Harrasment', 'Discrimination', 'Fraud'],
        q2 = [1, 2, 3],
        q3 = [1, 2, 1],
        ))


    c1, c2 = st.columns((7,3))
    with c1:
        st.markdown('### Plot by region')
        plost.time_hist(
        data=seattle_weather,
        date='date',
        x_unit='week',
        y_unit='day',
        color=time_hist_color,
        aggregate='median',
        legend=None,
        height=345,
        use_container_width=True)
    with c2:
        st.markdown('### Reports by type')
        plost.donut_chart(
            data=cases,
            theta=donut_theta,
            color='company',
            legend='bottom', 
            use_container_width=True)

    # Row C
    st.markdown('### Insert Bar Chart')
    st.line_chart(seattle_weather, x = 'date', y = plot_data, height = plot_height)
    

    
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')




  