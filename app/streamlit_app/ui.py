
# streamlit_app.py
import streamlit as st
import requests

st.title("AI Support Agent Chat")

user_input = st.text_input("You:")

if st.button("Send"):
    response = requests.post("http://localhost:8000/chat", json={"message": user_input})
    if response.ok:
        st.text("Bot: " + response.json().get("response", ""))
    else:
        st.text("Error communicating with agent API")
