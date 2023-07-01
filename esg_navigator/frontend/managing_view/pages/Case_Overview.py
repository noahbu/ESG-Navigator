import streamlit as st
from streamlit_chat import message

st.title('Hello World!')

if st.session_state["authentication_status"]:
    #st.info("You can now access the app.")
    with st.sidebar:
        st.session_state['authenticator'].logout("Logout", "sidebar")
        st.sidebar.title("Ucomply - Your Social Copilot")
        st.sidebar.write(f"Welcome {st.session_state['username']}!")


    st.header(f"Chat functionality")

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    if "user_input" not in st.session_state:
        st.session_state['user_input'] = ""

    chat_placeholder = st.empty()

    with chat_placeholder.container():   
        for i in range(len(st.session_state['chat_history'])):  
            chat = st.session_state['chat_history'][i]        
            message(chat["message"], is_user=chat["is_officer"], key=f"{i}_user")

    def on_input_change(is_officer):

        user_input = st.session_state.user_input
        data = {
                "timestamp": datetime.datetime.now(),
                "is_officer": is_officer,
                "message": user_input
            }
        st.session_state.chat_history.append(data)
        complaint_id = "1234"
        chat_to_csv(complaint_id, st.session_state.chat_history)


    with st.container():
        st.session_state.user_input = st.text_input("User Input:")
        if st.button("Submit message"):
            on_input_change(is_officer = True)


          # align's the message to the right





elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

        