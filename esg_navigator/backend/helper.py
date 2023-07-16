import streamlit as st
from streamlit_chat import message
import os
import yaml
from yaml.loader import SafeLoader 
import pandas as pd
import streamlit_authenticator as stauth
import datetime
import base64



def add_logo():
    """Adds the Ucomply logo to the sidebar"""

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
    """Loads the CSS file"""

    # Get the current script's directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Construct the full path to the CSS file
    file_path = os.path.join(dir_path, 'styles.css')

    with open(file_path, "r") as f:
        return f.read()
    

def app_init():
    """Initializes the app"""


    #Add logo to the sidebar
    add_logo()


    # Load the login module
    parent_directory = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    file_path = os.path.join(parent_directory, 'config.yaml')
    #st.write(file_path)

    with open(file_path) as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    
    if 'authenticator' not in st.session_state:
        st.session_state['authenticator'] = authenticator

    #name, authentication_status, username = authenticator.login('Login', 'main')
    st.session_state['name'], st.session_state['authentication_state'], st.session_state['username'] = authenticator.login('Login', 'main')


@st.cache_data

def load_complaints_db():
    """Loads the complaints database"""

    parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(parent_directory,"esg_navigator/data", "complaints_db.csv")

    st.session_state['complaints_db'] = pd.read_csv(file_path,sep= ";")

@st.cache_data
def load_manager_data():

    #TODO: Merge both databases
    """Loads the manager database"""

    parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(parent_directory,"esg_navigator/data", "complaints_db.csv")

    #Read database from csv
    db = pd.read_csv(file_path,sep= ";", index_col=False)
    #Filter by assigned responsible
    sliced_db = db[db['assigned_responsible'] == st.session_state['name']]

    if 'manager_db' not in st.session_state:
        st.session_state['manager_db'] = sliced_db
    else:
        st.session_state['manager_db'] = sliced_db

        return


#Chat helper functions 
@st.cache_data
def load_chat_history(id):
    """ Loads the chat history from the individualcsv file
    Args:
        id (int): id of the complaint
        
    Returns: 
        session_state['chat_history'] (list): list of dictionaries with the chat history
        """

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
    """Adds the user input to the chat history
    Args:
        id (int): id of the complaint
        is_officer (bool): True if the user is an officer, False if the user is a manager
    Returns:
        None
    """
    load_complaints_db()
    if not is_officer:
        st.session_state['complaints_db'].loc[st.session_state['complaints_db']['ID'] == id, 'new_message'] = True
    else:
        st.session_state['complaints_db'].loc[st.session_state['complaints_db']['ID'] == id, 'new_message'] = False

    write_to_complaints_db()

    user_input = st.session_state.user_input
    data = {
            "timestamp": datetime.datetime.now(),
            "is_officer": is_officer,
            "message": user_input
        }
    st.session_state.chat_history.append(data)
    #message(data["message"], is_user = data["is_officer"]) 
    chat_to_csv(str(id), st.session_state.chat_history)



def chat_to_csv(id,chat_history):
    
    """Writes the chat history to a csv file
    Args:
        id (int): id of the complaint
        chat_history (list): list of dictionaries with the chat history
    Returns:
        None    
        """

    parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(parent_directory,"esg_navigator/data/chats", str(id) + "_chat_history.csv")
    print(file_path)
    df = pd.DataFrame(chat_history)

    print(df)

    if os.path.isfile(file_path):
        os.remove(file_path)
    # Write the DataFrame to a CSV file (this will create a new file)
    df.to_csv(file_path,sep= ";", index=False)


def write_to_complaints_db():
    """
    
    """
    parent_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(parent_directory,"esg_navigator/data/complaints_db.csv")
    print(file_path)
    df = st.session_state['complaints_db']

    if os.path.isfile(file_path):
        os.remove(file_path)

    df.to_csv(file_path,sep= ";", index=False)




def displayPDF(file):
    # Opening file from file path
    if os.path.isfile(file):
        with open(file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')

        # Embedding PDF in HTML
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
        st.write("Documents loaded successfully")
        # Displaying File
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.write("No documents available yet!")



