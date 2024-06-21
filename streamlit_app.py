import google.generativeai as genai
#https://medium.com/@speaktoharisudhan/building-a-gemini-powered-chatbot-in-streamlit-e241ed5958c4
#from openai import OpenAI
import streamlit as st

with st.sidebar:
    gemini_api_key = st.text_input("Gemini API Key", key="chatbot_api_key", type="password")
    genai.configure(api_key= gemini_api_key)
    #"[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/Roland-N/gemini-app/blob/main/streamlit_app.py)"

st.title("💬 Gemini Pro Assistant")
st.caption("🚀 A Streamlit chatbot powered by Gemini")
#model = genai.GenerativeModel("gemini-1.5-flash") 
generation_config = {
  "temperature": 1,
  #"top_p": 0.95,
  #"top_k": 64,
  "max_output_tokens": 500,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="You are a professional data analyst mastering a variety of data tasks",
)
#chat = model.start_chat()
chat_session = model.start_chat(
  history=[
  ]
)



user_quest = st.text_input("Ask a question:")
btn = st.button("Generér")
#if btn and user_quest:
    #result = LLM_Response(user_quest)
   # response = chat_session.send_message(user_quest)
   # st.subheader("Svar: ")
    #st.text(response.text)
if btn and user_quest:
    # result = LLM_Response(user_quest)
    response = chat_session.send_message(user_quest)
    st.subheader("Svar: ")
    st.text_area("Response", response.text, height=1600)
