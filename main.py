import streamlit as st
from langchain_openai import OpenAI
from python import OPENAI_API_KEY

llm = OpenAI(api_key=OPENAI_API_KEY)

st.title("Langchain Demo with OpenAI")

promt = st.text_input("Enter a prompt: ")

if promt:
    response = llm.predict(promt)
    st.write(response)
    