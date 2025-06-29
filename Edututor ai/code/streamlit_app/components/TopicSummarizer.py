import streamlit as st
import requests

def summarizer_ui():
    st.header("📚 Topic Summarizer")
    topic = st.text_input("Enter topic to summarize:")
    if st.button("Summarize"):
        prompt = f"Summarize the topic '{topic}' in simple terms for Class 10 students."
        res = requests.post("http://127.0.0.1:8000/ask/", json={"prompt": prompt})
        st.success(res.json()['response'])
