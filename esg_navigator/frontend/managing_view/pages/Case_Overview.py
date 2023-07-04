import streamlit as st
from streamlit_chat import message
import datetime
from esg_navigator.backend.helper import add_logo, chat_to_csv, load_chat_history, load_manager_data, on_input_change
#from random_username.generate import generate_username

st.set_page_config(
    page_title=" Welcome to Ucomply - Your Social Copilot",
    page_icon="👋",
    layout="centered"
)

add_logo()

st.title('Active Cases')
st.header("Displaying all active cases")





if "user_input" not in st.session_state:
        st.session_state['user_input'] = ""


st.write("View your open cases")


if st.session_state["authentication_status"]:

    #st.info("You can now access the app.")
    with st.sidebar:
        st.session_state['authenticator'].logout("Logout", "sidebar")
        st.sidebar.title("Ucomply - Your Social Copilot")
        st.sidebar.write(f"Welcome {st.session_state['username']}!")

    load_manager_data()
    db = st.session_state['manager_db']

    st.data_editor(st.session_state['manager_db'])

    st.write("Select a case to view the status of your report")
    
    complainee = st.empty()
    case = complainee.selectbox("Select a case", st.session_state['manager_db']['name'].unique())
    st.write(case)


    st.divider()
    st.header(f"Complainee Interaction")
    case_id = db.loc[db['name'] == case, 'ID'].values[0]
    load_chat_history(case_id)    
    
    chat_placeholder = st.empty()

    with chat_placeholder.container():   
        for i in range(len(st.session_state['chat_history'])):  
            chat = st.session_state['chat_history'][i]        
            message(chat["message"], is_user = chat["is_officer"], key=f"{i}_user")

    with st.container():
        st.session_state.user_input = st.text_input("Generate your Response:")
        if st.button("Submit message"):
            
            on_input_change(case_id, is_officer = True)


          # align's the message to the righ



elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

        