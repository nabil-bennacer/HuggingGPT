import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

def get_gemini_chat_model(model_name: str = "gemini-2.5-flash") -> ChatGoogleGenerativeAI:
    load_dotenv()
    if "GEMINI_API_KEY" not in os.environ:
        raise ValueError("La clé n'est pas définie.")
    
    api_key = os.getenv("GEMINI_API_KEY")
    
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        google_api_key=api_key,
        temperature=0.7
    )