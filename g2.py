# Importing necessary libraries
from dotenv import load_dotenv
import streamlit as st
import os
import textwrap
import google.generativeai as genai
from streamlit_chat import message  # To make the chat UI more visually appealing

# Load environment variables
load_dotenv()

# Configure Google API key for Gemini AI
genai.configure(api_key="AIzaSyBA3AX4aOAF5YxsURWJOG3bdU-M47vT61w")

# Function to load the Gemini AI model and get responses
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(question)
    return response.text

# Initialize Streamlit app configuration
st.set_page_config(page_title="Gemini Q&A Chatbot", page_icon="🤖", layout="wide")

# Adding custom CSS styling for the chatbot
st.markdown("""
    <style>
    .chatbot-container {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }
    .input-container {
        margin-bottom: 20px;
    }
    .title {
        color: #4CAF50;
        font-weight: bold;
        text-align: center;
    }
    .message-bubble {
        border-radius: 15px;
        padding: 10px;
        margin: 10px 0;
        display: inline-block;
    }
    .user-bubble {
        background-color: #dcf8c6;
        color: #333;
        text-align: left;
    }
    .bot-bubble {
        background-color: #ececec;
        color: #333;
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True)

# Chatbot header
st.markdown("<h1 class='title'>ProboTutor - Q&A Chatbot using Gemini AI</h1>", unsafe_allow_html=True)

# Initialize session state to store chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Get user input
input_text = st.text_input("You:", key="input")

# Submit button to trigger chatbot response
if st.button("Send"):
    if input_text:
        # Store user query
        st.session_state.chat_history.append({"message": input_text, "is_user": True})
        
        # Get the chatbot response
        response = get_gemini_response(input_text)
        
        # Store bot response
        st.session_state.chat_history.append({"message": response, "is_user": False})

# Display the chat history
if st.session_state['chat_history']:
    with st.container():
        for index, chat in enumerate(st.session_state['chat_history']):
            if chat['is_user']:
                message(chat['message'], is_user=True, key=f"user_{index}")
            else:
                message(chat['message'], is_user=False, key=f"bot_{index}")


# Sidebar for additional information
with st.sidebar:
    st.markdown("### About ProboTutor - Q&A Chatbot using Gemini AI")
    st.markdown("""
        The Gemini AI Chatbot is powered by **Google's ProboTutor - Q&A Chatbot using Gemini AI** to provide intelligent, real-time responses to your questions.
        It uses state-of-the-art Generative AI models to generate thoughtful answers based on your input.
    """)
    st.markdown("#### Features:")
    st.markdown("""
        - Interactive Q&A
        - Powered by Google Generative AI (Gemini)
        - Responsive and sleek UI
    """)
