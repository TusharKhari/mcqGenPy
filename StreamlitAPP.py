import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_files, get_table_data
import streamlit as st
# from langchain.callbacks import get_openai_callback
from langchain_community.callbacks.manager import get_openai_callback
from src.mcqgenerator.logger import logging
from src.mcqgenerator.MCQGenerator import get_quiz_data


with open('Response.json') as file :
    RESPONSE_JSON = json.load(file)
    
st.title("Mcq generator application with LangChain")

with st.form("user_inputs"):
    uploaded_file=st.file_uploader("Upload a PDF or txt file")
    
    
    # input fields 
    mcq_count = st.number_input("No. of MCQs", min_value=3, max_value=50)
 
    #subject
    subject=st.text_input("Insert Subject", max_chars=20)

    # quiz tone
    tone=st.text_input("Complexity Level Of Questions", max_chars=20, placeholder="Simple")

    # add button
    button = st.form_submit_button("Create MCQs")
    
    
    # check if the button is clicked and all fields have input
    
    # if button and uploaded_file is not None and mcq_count and subject and tone:
    #     with st.spinner("loading"):
            # try
            
    if button:
        quiz = get_quiz_data()
        st.write(quiz)