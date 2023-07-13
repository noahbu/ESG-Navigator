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


st.markdown("""
Welcome to uComply!

On the Education page you can learn all about different forms of misconduct. 
You can also file a report with us, to tell us about misconduct in your company. Positive Feedback is appreciated as well, so we can management what they are doing good!

""")


