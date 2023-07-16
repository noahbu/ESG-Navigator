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
        #Load the database into the session state
    load_manager_data()
    #Get the database from the session state
    db = st.session_state['manager_db']


    st.title('Manage your active cases Cases')

    # This months complaints 

    #Retireve the amount of new_messages == True
    new_messages = db.loc[db['new_message'] == True, 'new_message'].count()
    new_message_db = db.loc[db['new_message'] == True,"case-name"]
    new_message_db_transposed = new_message_db.to_frame().T
    
    #Case_Overview Build: 
    col1, col2= st.columns(2)
    with(col1):
        st.metric("You have new unread messages for the following cases:", str(new_messages), 2)
    with(col2):
        st.write(new_message_db_transposed)

    st.write("")
    #Display the status of the case
    complainee = st.empty()
     #Drop-down for complaint handling
    case = complainee.selectbox("Select a case to view the status of your report", st.session_state['manager_db']['case-name'].unique())

   # Get the row where 'case-name' is 'case'
    row = db[db['case-name'] == case]
    timestamp = row['Timestamp'].iloc[0]
    case_id = row['ID'].iloc[0]
    st.write(case_id)
    urgency = row['Urgency'].iloc[0]
    anonymity = row['Anonymity'].iloc[0]
    email = row['Email'].iloc[0]
    category = row['Category'].iloc[0]
    location = row['Location'].iloc[0]
    issue = row['Issue'].iloc[0]
    evidence = row['Evidence'].iloc[0]
    case_name = row['case-name'].iloc[0]
    status = row['Status'].iloc[0]
    region = row['Region'].iloc[0]


    # Store each column's value in a separate variable

    col1, col2 = st.columns(2,gap = "large")
    with(col1):
        st.header("**User Information**")
        if anonymity == 'Anonymous':
            st.write("Name : Anonymous")
        else:
            st.write("Name : ", email)
    with(col2):
        st.header("**Case Information**")
        st.write("Case Status : ", status)
        st.write("Urgency : ", urgency)
        st.write("Time of the Incident: ", timestamp)
        st.write("Location : ", region)

    #Display editable table
    st.write("Edit the case information below")
    st.data_editor(st.session_state['manager_db'][st.session_state['manager_db']['case-name'] == case])

    #Filter open complaints by region for Germany

    st.divider()

    #Chat functionality
    st.header(f"Complainee Interaction")
    st.write("Chat with the complainee to resolve the case")
    st.write("")

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

        