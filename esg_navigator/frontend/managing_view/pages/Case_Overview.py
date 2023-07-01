import streamlit as st
from streamlit_chat import message

st.title('Hello World!')

if st.session_state["authentication_status"]:
    #st.info("You can now access the app.")
    with st.sidebar:
        st.session_state['authenticator'].logout("Logout", "sidebar")
        st.sidebar.title("Ucomply - Your Social Copilot")
        st.sidebar.write(f"Welcome {st.session_state['username']}!")


          # align's the message to the right





elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

        