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


def generate_text_from_img(file_path):
    pass

def generate_story_from_text(text):
    pass



def generate_speech_from_text(text):
    pass



def main():

    st.set_page_config(page_title= "IMAGE TO STORY CONVERTER", page_icon= "🖼️")

    st.header('Image to Speech Generator')
    st.write('This app uses a combination of AI models to generate a short story from an image .')
    st.write('Please upload an image to get started .')

    
    with st.sidebar:
        st.image("aud-img/person.png")
        st.write("---")
        st.write("AI App created by @ Kanishka Rani")


    uploaded_file=st.file_uploader('Choose a file to upload',type='png')
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image",
                 use_column_width=True)
        bytes_data:Any=uploaded_file.getvalue()
        with open (uploaded_file.name,'wb') as file:
            file.write(bytes_data)
            file.close()
        progress_bar(100)
        
        scenario:str=generate_text_from_img(uploaded_file.name)
        story:str=generate_story_from_text(scenario)
        generate_speech_from_text(story)

        with st.expander('Generated Image Scenario'):
            st.write(scenario)
        with st.expander('Generated Short Story'):
            st.write(story)

        st.audio('Generated_Audio.flac')

    else:
        st.warning("Please upload an image to get started .")

if __name__ == "__main__":
    main()