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


def generate_text_from_img(file_path:str)->str:
    image_to_text = pipeline(
        "image-to-text",
        model="Salesforce/blip-image-captioning-base",
        device=0
    )

    text:str=image_to_text(file_path)[0]['generated_text']

    print(f'Image url{file_path}')
    print(f'Generated text {text}')
    return text

def generate_story_from_text(text):
    prompt_template:str=f'''

    Your are a talented story writer . WHo can create a story from a simple narrative ./
    You have to create a story from the following text but the story must be minimum of 50 words it must be interesting while reading :
    CONTEXT:{text}
    STORY:
    '''

    prompt=PromptTemplate(template=prompt_template,input_variables=['text'])
    llm=ChatGroq(api_key=GROQ_API_KEY,model='llama-3.3-70b-versatile')
    story_llm: Any = LLMChain(llm=llm, prompt=prompt, verbose=True)
    generated_story: str = story_llm.predict(text=text)

    print(f"TEXT INPUT: {text}")
    print(f"GENERATED STORY OUTPUT: {generated_story}")
    return generated_story



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
                 use_container_width=True)
        bytes_data:Any=uploaded_file.getvalue()
        with open (uploaded_file.name,'wb') as file:
            file.write(bytes_data)
            file.close()
        progress_bar(100)

        
        scenario:str=generate_text_from_img(uploaded_file.name)
        story:str=generate_story_from_text(scenario)
        with st.expander('Generated Short Story'):
            st.write(story)


    else:
        st.warning("Please upload an image to get started .")

if __name__ == "__main__":
    main()