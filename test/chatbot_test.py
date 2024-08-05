import pytest
import streamlit as st
from src import chatbot

@pytest.fixture
def session_state_setup():
    st.session_state.clear()
    st.session_state.messages = []
    st.session_state.chats = []
    st.session_state.chat_num = 0

def test_new_chat(session_state_setup):
    st.session_state.messages.append({"role": "user", "content": "Hello"})
    chatbot.new_chat()
    assert len(st.session_state.chats) == 1
    assert st.session_state.chats[0] == [{"role": "user", "content": "Hello"}]
    assert st.session_state.messages == []
    assert st.session_state.chat_num == 1

def test_create_msg_user(session_state_setup):
    chatbot.create_msg("user", "Hello")
    assert len(st.session_state.messages) == 1
    assert st.session_state.messages[0] == {"role": "user", "content": "Hello"}

def test_create_msg_ai(session_state_setup, mocker):
    mocker.patch('streamlit.chat_message')  
    chatbot.create_msg("ai", "Hi there!")
    assert len(st.session_state.messages) == 1
    assert st.session_state.messages[0] == {"role": "ai", "content": "Hi there!"}
