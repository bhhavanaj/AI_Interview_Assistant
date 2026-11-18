import streamlit as st
from groq import Groq
st.set_page_config(page_title='LLM',layout='centered')
st.title('AI Interview')
st.caption('Practice and Prepare for your interview')
try:
  client = Groq(api_key = st.secrets("GROQ_API_KEY"))
except ( Keyerror,FileNotFound):
  st.error("API Key is missing.Add it in Advanced settings")
  st.stop()
