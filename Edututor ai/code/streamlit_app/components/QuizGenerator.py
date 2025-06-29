import streamlit as st
import requests
import random

def quiz_ui():
    st.header("🧠 Quiz Generator")
    topic = st.text_input("Enter topic or content:")

    if st.button("Generate Quiz"):
        prompt = f"Create 5 unique quiz questions from the topic: {topic} with 4 options and answers. Avoid repeating questions."
        res = requests.post("http://127.0.0.1:8000/ask/", json={"prompt": prompt})
        st.info(res.json()["response"])
