import os
from langchain_openai import ChatOpenAI 
import streamlit as st
import time

os.environ["OPENAI_API_KEY"] = "sk-proj-S1BI7CLEpE9ISnNeEdSoT3BlbkFJ5siFAJjc2XbPJjdPEMoT"

llm = ChatOpenAI(model = "gpt-3.5-turbo")

def new_chat():
    if len(st.session_state.chats) == st.session_state.chat_num:
        st.session_state.chats.append(st.session_state.messages.copy())
    else:
        st.session_state.chats[st.session_state.chat_num] = st.session_state.messages.copy()
    st.session_state.messages.clear()
    st.session_state.chat_num = len(st.session_state.chats)

def stream(msg: str):
    for word in msg.split(" "):
        yield word + " "
        time.sleep(0.12)

def create_msg(author: str, msg: str):
    if author == "ai":
        st.chat_message(author).write_stream(stream(msg))
    else:
        st.chat_message(author).markdown(msg)
    st.session_state.messages.append({"role":author,"content":msg})

st.title("TestAI")

sidebar = st.sidebar
new_chat_button = sidebar.button("New chat")
if new_chat_button:
    new_chat()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chats" not in st.session_state:
    st.session_state.chats = []

if "chat_num" not in st.session_state:
    st.session_state.chat_num = 0

for chat in range(len(st.session_state.chats)):
    if sidebar.button(f"Chat {chat}"):
        st.session_state.messages = st.session_state.chats[chat]
        st.session_state.chat_num = chat

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Write here"):
    create_msg("user",prompt)
    ai_resp = llm.invoke(st.session_state.messages)
    if ai_resp:
        create_msg("ai", ai_resp.content)