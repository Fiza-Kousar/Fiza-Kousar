# 📘 ML-Powered Digital Slam Book using Streamlit + Gemini + HuggingFace

import streamlit as st
from transformers import pipeline
import random
import json
import os
import google.generativeai as genai

# Load Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

# Emotion classifier (HuggingFace pipeline)
sentiment_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

# Load teammate messages (mock data)
with open("messages.json", "r") as f:
    messages = json.load(f)

# Shuffle messages each time
random.shuffle(messages)

st.set_page_config(page_title="Team Slam Book", layout="centered")
st.title("📖 Digital Slam Book for Our Amazing Team Lead")

# Show one message per page, with navigation
if "page" not in st.session_state:
    st.session_state.page = 0

# Navigation
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⬅️ Previous"):
        st.session_state.page = max(0, st.session_state.page - 1)
with col3:
    if st.button("Next ➡️"):
        st.session_state.page = min(len(messages) - 1, st.session_state.page + 1)

# Current message
data = messages[st.session_state.page]
name = data["name"]
message = data["message"]

# Emotion detection
emotion = sentiment_pipeline(message)[0]["label"]

# Gemini prompt
prompt = f"""
Create a warm, heartfelt farewell note to a beloved team lead.
Use the message from teammate {name}: \"{message}\".
Make it emotional, expressive, and appreciative.
"""
gemini_response = model.generate_content(prompt)
summary = gemini_response.text

# Display slam book page
st.markdown("---")
st.subheader(f"👤 From: {name}")
st.text_area("📝 Message:", value=message, height=150, disabled=True)
st.markdown(f"**🎭 Detected Emotion:** `{emotion}`")
st.markdown("---")
st.markdown("#### 💌 Gemini's Enhanced Message")
st.markdown(summary)

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit, HuggingFace, and Gemini")
