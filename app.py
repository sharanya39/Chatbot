import streamlit as st
from chatbot import get_chatbot_response

# Streamlit page config
st.set_page_config(page_title="Langchain + Groq Chatbot", page_icon="🤖")

st.title("🤖 Langchain Chatbot powered by Groq")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input box
if user_input := st.chat_input("Ask me anything"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Get response from chatbot
    response = get_chatbot_response(user_input)

    # Add bot message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display bot message
    with st.chat_message("assistant"):
        st.write(response)
