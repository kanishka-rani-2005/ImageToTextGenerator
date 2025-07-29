import os
import time
from typing import Any
import requests 
import json
import streamlit as st

from dotenv import load_dotenv

from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate 
from transformers import pipeline 

load_dotenv()


HUGGINGFACE_API_TOKEN=os.getenv('HUGGINGFACE_API_TOKEN')
GROQ_API_KEY=os.getenv('GROQ_API_KEY')

## Create one progress bar 
def progress_bar(amt_of_time)->Any:
    progress_text='Please wait , Generative models hard to work.'
    my_bar=st.progress(0,text=progress_text)

    for i in range(amt_of_time):
        time.sleep(0.04)
        my_bar.progress(i+1,progress_text)
    time.sleep(1)
    my_bar.empty()




def main():

    st.set_page_config(page_title= "IMAGE TO STORY CONVERTER", page_icon= "🖼️")

    st.title('Image to Speech Generator')
    st.write('This app uses a combination of AI models to generate a short story from an image .')
    


if __name__ == "__main__":
    main()