import streamlit as st
from streamlit_chat import message
import os
import yaml
from yaml.loader import SafeLoader 
import pandas as pd
import streamlit_authenticator as stauth
import datetime


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://i.imgur.com/AU2IgZs.png?1);
                background-repeat: no-repeat;
                padding-top: 60px;
                background-position: 35px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                margin-left: 30px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 200px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

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
    



def app_init():

    with open('../../config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    add_logo()
    if 'authenticator' not in st.session_state:
        st.session_state['authenticator'] = authenticator

    #name, authentication_status, username = authenticator.login('Login', 'main')
    st.session_state['name'], st.session_state['authentication_state'], st.session_state['username'] = authenticator.login('Login', 'main')



@st.cache_data
def load_complaints_db():

    parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(parent_directory, 'data', 'complaints_db.csv')
    st.session_state['complaints_db'] = pd.read_csv(file_path,sep= ";")

@st.cache_data
def load_manager_data():
    parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(parent_directory,"esg_navigator/data", "manager_db.csv")
    db = pd.read_csv(file_path,sep= ";")
    sliced_db = db[db['assigned_responsible'] == st.session_state['name']]

    if 'manager_db' not in st.session_state:
        st.session_state['manager_db'] = sliced_db
    else:

        return


#Chat helper functions 
@st.cache_data
def load_chat_history(id):

    parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    file_path = os.path.join(parent_directory,"esg_navigator/data/chats", str(id) +"_chat_history.csv")
    if os.path.isfile(file_path):
        db = pd.read_csv(file_path,sep= ";")
        list_dict = db.to_dict('records')
        st.session_state['chat_history'] = list_dict
    else:
        st.session_state['chat_history'] = []

    return 

def on_input_change(id, is_officer):

            user_input = st.session_state.user_input
            st.write(f"User input: {user_input}")
            data = {
                    "timestamp": datetime.datetime.now(),
                    "is_officer": is_officer,
                    "message": user_input
                }
            st.session_state.chat_history.append(data)
            message(data["message"], is_user = data["is_officer"]) 
            chat_to_csv(str(id), st.session_state.chat_history)


##TODO
def chat_to_csv(id,chat_history):
    parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(parent_directory,"esg_navigator/data/chats", str(id) + "_chat_history.csv")
    print(file_path)
    df = pd.DataFrame(chat_history)

    print(df)

    if os.path.isfile(file_path):
        os.remove(file_path)
    # Write the DataFrame to a CSV file (this will create a new file)
    df.to_csv(file_path,sep= ";", index=False)




