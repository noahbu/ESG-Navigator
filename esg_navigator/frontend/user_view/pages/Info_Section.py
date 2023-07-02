import streamlit as st
from esg_navigator.backend.helper import add_logo


st.set_page_config(
    page_title="Info-Section",
    page_icon="👋",
    layout="wide"
)
add_logo()  


def load_assets():
    # Load CSS
    css_file_path = os.path.join(os.path.dirname(__file__), "styles.css")
    with open(css_file_path, "r") as f:
        css = f.read()

    # Load JavaScript
    js_file_path = os.path.join(os.path.dirname(__file__), "fixes.js")
    with open(js_file_path, "r") as f:
        js = f.read()


st.title('About')


st.write("""
We are THE whistelblowing and complaints handling platform. 
Everything you share with us will be handled confidentially and only shared anonymously with management to change the circumstances. 
However under spcific circumstances we can create a direct line of communication with the upper management to address any misbehaviours. 
""")
