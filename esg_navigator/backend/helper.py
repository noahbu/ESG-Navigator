import streamlit as st
import os
def load_css():

    """file_path = os.path.join(os.path.dirname(__file__), "../styles.css")
    with open(file_path, "r") as f:
        css = f.read()
    return css
    """
    # Get the current script's directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Construct the full path to the CSS file
    file_path = os.path.join(dir_path, 'styles.css')

    with open(file_path, "r") as f:
        return f.read()
    

def load_manager_data():
    parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(parent_directory, 'data', 'complaints_db.csv')
    st.session_state['complaints_db'] = pd.read_csv(file_path,sep= ";")




def session_states_init():
    if 'user' not in st.session_state:
        st.session_state['user'] = ''
    if 'username' not in st.session_state:
        st.session_state['username'] = ''
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_state'] = False
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = "Home"
