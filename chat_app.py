import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import re
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")


# Initialize conversation if it doesn't exist
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

st.title("Welcome to Gemini-Pro")
user_input = ""


def main():
    chat = model.start_chat()

    # Use st.markdown to display conversation history with avatars
    st.markdown("**Conversation History**")
    for entry in st.session_state.conversation:
        if entry.startswith('You:'):
            st.image('download.jpg', width=200, caption=entry)
        elif entry.startswith('🤖:'):
            st.image('goog.jpg', width=200, caption=entry)

    # Create a space between user input and model response
    st.markdown("---")

    # Use st.text_input to get user input (fixed at the bottom)
    user_input = st.text_input("You:")

    if st.button("Send"):
        # Send user input to the model
        response = chat.send_message(user_input, )

        # Add user input to the conversation history
        st.session_state.conversation.append(f'You: {user_input}')

        # Display model response line by line
        model_response_lines = re.split(r'(?<=[.!?]) ', response.text)
        for line in model_response_lines:
            st.session_state.conversation.append(f'🤖: {line}')


if __name__ == "__main__":
    main()
