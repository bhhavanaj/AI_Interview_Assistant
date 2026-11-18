import streamlit as st
from groq import Groq
st.set_page_config(page_title='LLM',layout='centered')
st.title('AI Interview')
st.caption('Practice and Prepare for your interview')
try: 
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError , FileNotFound):
  st.error("API key is missing . Add it in Advanced setting")
  st.stop()
