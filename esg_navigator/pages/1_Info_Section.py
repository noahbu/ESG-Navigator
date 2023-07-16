import streamlit as st
from esg_navigator.backend.helper import add_logo


st.set_page_config(
    page_title="Info-Section",
    page_icon="👋",
    layout="wide"
)
#Add-Logo to the sidebar
add_logo()  
#Add signature to the sidebar
st.sidebar.markdown('''
        ---
        Created with ❤️ by UComply.
        ''')


#Add title to the page and a short description
st.title('About')
st.markdown("""
Welcome to uComply!

On the **Education page** you can learn all about different forms of misconduct. 
You can also file a report with us, to tell us about misconduct in your company. Positive Feedback is appreciated as well, so we can management what they are doing good!
""")
            


