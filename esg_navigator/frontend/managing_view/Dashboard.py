import streamlit as st
import streamlit_authenticator as stauth
import pickle
from pathlib import Path
import pandas as pd
import os
from streamlit_option_menu import option_menu
import yaml
from yaml.loader import SafeLoader 
from esg_navigator.backend.helper import app_init,load_css, load_complaints_db,load_manager_data
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

app_init()


if st.session_state["authentication_status"]:

    load_manager_data()

    st.title("UComply Dashboard")
    st.write("View your open cases")
    st.dataframe(st.session_state['manager_db'])
    st.session_state['authenticator'].logout("Logout", "sidebar")
    #st.info("You can now access the app.")
    with st.sidebar:
        
        st.title("Ucomply - Your Social Copilot")
        st.write(f"Welcome {st.session_state['username']}!")
    
        st.header('Dashboard `version 2`')

        st.sidebar.subheader('Heat map parameter')
        time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 

        st.sidebar.subheader('Donut chart parameter')
        donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

        st.sidebar.subheader('Line chart parameters')

        plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
        plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

        st.sidebar.markdown('''
        ---
        Created with ❤️ by [Data Professor](https://youtube.com/dataprofessor/).
        ''')


    # Row A
    st.markdown('### Metrics')
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")

    # Row B
    seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
    stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

    c1, c2 = st.columns((7,3))
    with c1:
        st.markdown('### Heatmap')
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
        st.markdown('### Donut chart')
        plost.donut_chart(
            data=stocks,
            theta=donut_theta,
            color='company',
            legend='bottom', 
            use_container_width=True)

    # Row C
    st.markdown('### Line chart')
    st.line_chart(seattle_weather, x = 'date', y = plot_data, height = plot_height)
    




   

    
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')




  