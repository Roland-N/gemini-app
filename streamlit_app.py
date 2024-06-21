import google.generativeai as genai
#https://medium.com/@speaktoharisudhan/building-a-gemini-powered-chatbot-in-streamlit-e241ed5958c4
#from openai import OpenAI
import streamlit as st
import PyPDF2


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

instruction_prompt = st.text_input("System instructions")
user_prompt = st.text_input("Ask a question:")
button = st.button("Generér")


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
pdf_file_path = './gemini-app/Documentation_test.pdf'

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
    return text

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_file_path)
print(pdf_text)  # Check the extracted text



if button and user_prompt:
    response = chat_session.send_message(user_prompt)
    st.subheader("Svar: ")
    st.markdown(response.text)
