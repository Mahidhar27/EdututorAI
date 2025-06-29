import streamlit as st
from components.Chatbot import chatbot_ui
from components.QuizGenerator import quiz_ui
from components.CodeHelper import code_ui
from components.TopicSummarizer import summarizer_ui

st.set_page_config(page_title="EduTutor AI", layout="centered")

st.markdown("## 🎓 EduTutor AI: Personalized Learning with Generative AI")
st.markdown("Select a feature below:")

# Add chat-style expandable sections instead of sidebar menu
with st.expander("💬 Chatbot – Ask Questions (Maths, English, Science)"):
    chatbot_ui()

with st.expander("🧠 Quiz Generator – Generate Random Quiz from Topic"):
    quiz_ui()

with st.expander("👨‍💻 Code Helper – Get Programming Help"):
    code_ui()

with st.expander("📚 Topic Summarizer – Summarize Class Topics"):
    summarizer_ui()
