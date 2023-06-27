import streamlit as st
import numpy as np
import secrets
import pandas as pd
from datetime import datetime
import os

st.set_page_config(
    page_title="Report Status",
    page_icon="👋",
    layout="wide"
)



st.title("Report Status")

process_id = st.text_input("Please enter your case ID to see the status of your report")
if st.button("Check Status"):
    st.write("Success!")


