import streamlit as st

st.set_page_config(page_title="AI Mental Health Chatbot", layout="centered")

st.title("AI Mental Health Companion")

st.write("Welcome! Use the sidebar to switch between:")
st.markdown("""
- **Module 1: Journaling**
- **Module 2: To-Do List**
- **Module 3: Agenda Completion & AI Trigger**
- **Module 4: AI Chatbot**
""")

st.info("Go to the left sidebar to access all modules.")