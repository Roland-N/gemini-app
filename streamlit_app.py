import google.generativeai as genai
#https://medium.com/@speaktoharisudhan/building-a-gemini-powered-chatbot-in-streamlit-e241ed5958c4
#from openai import OpenAI
import streamlit as st

with st.sidebar:
    gemini_api_key = st.text_input("Gemini API Key", key="chatbot_api_key", type="password")
    genai.configure(api_key= gemini_api_key)
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Gemini Pro Assistant")
st.caption("🚀 A Streamlit chatbot powered by Gemini")
model = genai.GenerativeModel("gemini-1.5-flash") 
chat = model.start_chat()

def LLM_Response(question):
    response = chat.send_message(question,stream=True)
    return response


user_quest = st.text_input("Ask a question:")
btn = st.button("Ask")

if btn and user_quest:
    result = LLM_Response("Act as a witty comedian and write a joke about this topic: ", user_quest)
    st.subheader("Response : ")
    for word in result:
        st.text(word.text)
