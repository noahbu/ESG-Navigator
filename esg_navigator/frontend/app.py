import streamlit as st
import streamlit_authenticator as stauth
import pickle
from pathlib import Path
import pandas as pd
import os

import yaml
from yaml.loader import SafeLoader 



st.set_page_config(
    page_title="Ucomply - Your Social Copilot",
    page_icon="👋",
    layout="centered"
)

def load_css():
    file_path = os.path.join(os.path.dirname(__file__), "styles.css")
    print(file_path)
    with open(file_path, "r") as f:
        css = f.read()
    return css

css_file = "styles.css"
css_content = load_css()
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)



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

st.session_state["name"] = name
st.session_state["authentication_status"] = authentication_status
st.session_state["username"] = username

if st.session_state["authentication_status"]:
    st.success("Logged in as: {}".format(name))
    #st.info("You can now access the app.")
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title("Ucomply - Your Social Copilot")
    st.sidebar.write(f"Welcome {username}!")
    
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')


  