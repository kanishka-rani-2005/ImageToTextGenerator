import os
import time
from typing import Any
import requests 
import json
import streamlit as st

from dotenv import load_dotenv

from langchain.chains import LLMChain
from langchain.groq import ChatGroq
from langchain.prompts import PromptTemplate 
from transformers import pipeline 

load_dotenv(find_dotenv())