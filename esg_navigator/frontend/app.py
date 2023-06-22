import streamlit as st
import streamlit_authenticator as stauth
import pickle
from pathlib import Path
import pandas as pd
import os
from streamlit_option_menu import option_menu
import yaml
from yaml.loader import SafeLoader 
from esg_navigator.backend.helper import load_css,session_states_init



st.set_page_config(
    page_title="Ucomply - Your Social Copilot",
    page_icon="👋",
    layout="centered"
)

#Session_state_init: 
#session_states_init()


with open('../config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
name, authentication_status, username = authenticator.login('Login', 'main')
st.write(f"Welcome {st.session_state.authentication_status}!")

st.session_state["name"] = name
st.session_state["authentication_status"] = authentication_status
st.session_state["username"] = username
st.session_state["authenticator"] = authenticator

st.write(f"Welcome {st.session_state.authentication_status}!")


if st.session_state["authentication_status"]:
    #st.info("You can now access the app.")
    with st.sidebar:
        authenticator.logout("Logout", "sidebar")
        st.sidebar.title("Ucomply - Your Social Copilot")
        st.sidebar.write(f"Welcome {username}!")

    selected3 = option_menu(None, ["Dashboard", "Complaints",  "Report", 'Settings'], 
                icons=['house', 'bookmarks', "save", 'gear'], 
                menu_icon="cast", default_index=0, orientation="horizontal",
                styles={
                    "container": {"padding": "0!important", "background-color": "#155D59"},
                    "icon": {"color": "orange", "font-size": "20px"}, 
                    "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#E9BD47"},
                    "nav-link-selected": {"background-color": "FFCB43"},
                }
            )    
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')




  