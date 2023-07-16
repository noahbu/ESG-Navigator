import streamlit as st
from streamlit_chat import message
import datetime
from backend.helper import add_logo, chat_to_csv, load_chat_history, load_manager_data, on_input_change
#from random_username.generate import generate_username

st.set_page_config(
    page_title=" Welcome to Ucomply - Your Social Copilot",
    page_icon="👋",
    layout="centered"
)
#Load logo to the sidebar
add_logo()



#Intialize session state variables
if "user_input" not in st.session_state:
        st.session_state['user_input'] = ""




if st.session_state["authentication_status"]:
    #Sidebar customization
    with st.sidebar:
        st.session_state['authenticator'].logout("Logout", "sidebar")
        st.sidebar.title("Ucomply - Your Social Copilot")
        st.sidebar.write(f"Welcome {st.session_state['username']}!")
        st.markdown('''
        ---
        Created with ❤️ by UComply.
        ''')



    st.title('Manage your active cases Cases')

    st.header("Overview of your active cases")
    # This months complaints 
    st.metric("You have new unread messages:", " 3")
    #Filter open complaints by region for Germany



    st.header("Displaying all active cases")

    st.write("View your open cases")


   

    #Load the database into the session state
    load_manager_data()
    #Get the database from the session state
    db = st.session_state['manager_db']

    #Display editable table
    st.data_editor(st.session_state['manager_db'])

    st.write("Select a case to view the status of your report")
    #Display the status of the case
    complainee = st.empty()

    #Drop-down for complaint handling
    case = complainee.selectbox("Select a case", st.session_state['manager_db']['case-name'].unique())


    st.write(case)

    st.divider()

    #Chat functionality
    st.header(f"Complainee Interaction")
    st.write("Chat with the complainee to resolve the case")
    st.write("")
    case_id = db.loc[db['case-name'] == case, 'ID'].values[0]

    #Load chat_history forthe case in question
    load_chat_history(case_id)    
    #Display chat history
    chat_placeholder = st.empty()
    #Load chat history
    with chat_placeholder.container():   
        for i in range(len(st.session_state['chat_history'])):  
            chat = st.session_state['chat_history'][i]        
            message(chat["message"], is_user = chat["is_officer"], key=f"{i}_user")

    #Text functionality
    with st.container():
        st.session_state.user_input = st.text_input("Generate your Response:")
        if st.button("Submit message"):
            on_input_change(case_id, is_officer = True)
            st.experimental_rerun()



          # align's the message to the righ



elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

        