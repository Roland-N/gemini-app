import google.generativeai as genai
#https://medium.com/@speaktoharisudhan/building-a-gemini-powered-chatbot-in-streamlit-e241ed5958c4
#from openai import OpenAI
import streamlit as st
import fitz  # PyMuPDF



with st.sidebar:
    gemini_api_key = st.text_input("Gemini API Key", key="chatbot_api_key", type="password")
    genai.configure(api_key= gemini_api_key)
    #"[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/Roland-N/gemini-app/blob/main/streamlit_app.py)"



st.title("💬 Gemini Pro Assistant")
st.caption("🚀 A Streamlit chatbot powered by Gemini")



def pdf_to_text(uploaded_file):
    # Upload to streamlit
    # Read the PDF file into bytes
    pdf_bytes = uploaded_file.getvalue()
    # Open the PDF with PyMuPDF (fitz) using the bytes
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])
if pdf_file is not None:
    text = pdf_to_text(pdf_file)

else:
    text = ""



options = ["option 1", "option 2", "Option 3"]

# Create the dropdown
selected_option = st.selectbox("Vælg en system instruktion:", options)
user_prompt = st.text_input("User prompt:")
button = st.button("Generate")
temperature = st.slider("Model temperature", 0.0, 2.0, 0.3, step=0.1)
st.write("Temperature:", temperature)


#model = genai.GenerativeModel("gemini-1.5-flash") 
generation_config = {
  "temperature": temperature,
  #"top_p": 0.95,
  #"top_k": 64,
  "max_output_tokens": 2500,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction= instruction_prompt,
)
#chat = model.start_chat()
chat_session = model.start_chat(
  history=[
  ]
)


# Path to the PDF file in the cloned repository



if button and user_prompt:
    response = chat_session.send_message(user_prompt + text)
    st.subheader("Svar: ")
    st.markdown(response.text)


# prompts

with st.expander("Read more about your role as a financial analysis expert"):
    st.write("""
   As a financial analysis expert, your role is to interpret complex financial data, offer personalized advice, and evaluate investments using statistical methods to gain insights across different financial areas.

Accuracy is the top priority. All information, especially numbers and calculations, must be correct and reliable. Always double-check for errors before giving a response.  The way you respond should change based on what the user needs. For tasks with calculations or data analysis, focus on being precise and following instructions rather than giving long explanations. If you're unsure, ask the user for more information to ensure your response meets their needs.

For tasks that are not about numbers:

* Use clear and simple language, avoiding jargon and confusion.
* Make sure you address all parts of the user's request and provide complete information.
* Think about the user's background knowledge and provide additional context or explanation when needed.

Formatting and Language:

* Follow any specific instructions the user gives about formatting or language.
* Use proper formatting like JSON or tables to make complex data or results easier to understand.
    """)
