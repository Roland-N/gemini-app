import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Roland's Gemini Assistant

checkout [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

test for working connection
"""

import google.generativeai as genai


genai.configure(api_key = "AIzaSyAg3REDWkGV7hyVJpOlZjtj73CjQi37TcQ")

model = genai.GenerativeModel("gemini-1.5-flash") 
chat = model.start_chat()

def LLM_Response(question):
    response = chat.send_message(question,stream=True)
    return response

st.title("Chat Application using Gemini Pro")

user_quest = st.text_input("Ask a question:")
btn = st.button("Ask")

if btn and user_quest:
    result = LLM_Response(user_quest)
    st.subheader("Response : ")
    for word in result:
        st.text(word.text)
