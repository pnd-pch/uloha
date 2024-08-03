import os
from langchain_openai import ChatOpenAI 
import streamlit as st

os.environ["OPENAI_API_KEY"] = "sk-proj-S1BI7CLEpE9ISnNeEdSoT3BlbkFJ5siFAJjc2XbPJjdPEMoT"

llm = ChatOpenAI(model = "gpt-3.5-turbo")

def create_msg(author: str, msg: str):
    st.chat_message(author).markdown(msg)
    st.session_state.messages.append({"role":author,"content":msg})

st.title("TestAI")

sidebar = st.sidebar

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_num" not in st.session_state:
    st.session_state.chat_num = 0
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Write here"):
    create_msg("user",prompt)
    ai_resp = llm.invoke(st.session_state.messages)
    if ai_resp:
        create_msg("ai", ai_resp.content)