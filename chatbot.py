import os
from langchain_openai import ChatOpenAI 
import streamlit as st

os.environ["OPENAI_API_KEY"] = "sk-proj-S1BI7CLEpE9ISnNeEdSoT3BlbkFJ5siFAJjc2XbPJjdPEMoT"

llm = ChatOpenAI(model = "gpt-3.5-turbo")

st.title("TestAI")

if prompt := st.chat_input("Write here"):
    st.chat_message("user").markdown(prompt)
    ai_resp = llm(prompt)
    if ai_resp:
        st.chat_message("ai").write(ai_resp.content)
    

