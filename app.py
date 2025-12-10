### Health Management APP
from dotenv import load_dotenv

load_dotenv()  ## load all the environment variables
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("gen-lang-client-0329794582"))
