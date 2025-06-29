import streamlit as st
import requests

def code_ui():
    st.header("👨‍💻 Code Helper")
    lang = st.selectbox("Choose Language", ["Python", "Java", "C++", "JavaScript"])
    topic = st.text_input("Enter topic (e.g., recursion, for loop):")

    if st.button("Explain"):
        prompt = f"Explain with examples about {topic} in {lang}."
        res = requests.post("http://127.0.0.1:8000/ask/", json={"prompt": prompt})
        st.success(res.json()['response'])
