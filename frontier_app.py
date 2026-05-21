import os
import gradio as gr
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")
chat_session = model.start_chat(history=[])

def chat_fn(message, history):
    global chat_session
    response = chat_session.send_message(message)
    return response.text

def clear_memory():
    global chat_session
    chat_session = model.start_chat(history=[])

demo = gr.ChatInterface(
    fn=chat_fn,
    title="Frontier Assistant - Gemini",
    description="Simple Gemini chatbot",
)

if __name__ == "__main__":
    demo.launch()