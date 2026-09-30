import streamlit as st
import ollama

st.title("🤖 AI Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input

user_input = st.chat_input("Type your message...", key="main_chat_input")

if user_input:

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Get response from Ollama
    response = ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
    )

    # Extract bot response
    bot_response = response["message"]["content"]

    # Add bot response to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })

    # Display bot response
    with st.chat_message("assistant"):
        st.write(bot_response)