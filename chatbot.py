import os
from langchain_openai import ChatOpenAI 
import streamlit as st

os.environ["OPENAI_API_KEY"] = "sk-proj-S1BI7CLEpE9ISnNeEdSoT3BlbkFJ5siFAJjc2XbPJjdPEMoT"

llm = ChatOpenAI(model = "gpt-3.5-turbo")

st.title("TestAI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Write here"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt})
    ai_resp = llm(prompt)
    if ai_resp:
        st.chat_message("ai").write(ai_resp.content)
        st.session_state.messages.append({"role":"ai","content":ai_resp.content})

