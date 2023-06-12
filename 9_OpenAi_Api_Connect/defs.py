import pandas as pd
import streamlit as st
import openai
import os
from dotenv import load_dotenv
import streamlit as st


# Connect to OpenAi
def oai_key():
    load_dotenv()
    API_KEY = os.getenv("API_KEY")    
    return(API_KEY)

# App Title
def app_title():
    app_title = st.title(" API_KEY_SET " )
    return(app_title)