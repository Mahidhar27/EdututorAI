import streamlit as st
import requests

def chatbot_ui():
    st.header("🤖 Ask Me Anything (Maths, English, Science)")
    question = st.text_input("Enter your doubt:")
    if st.button("Ask"):
        if question:
            res = requests.post("http://127.0.0.1:8000/ask/", json={"prompt": question})
            st.success(res.json()['response'])
