import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def get_gemini_embeddings(model_name: str | None = None) -> GoogleGenerativeAIEmbeddings:
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("La variable d'environnement GEMINI_API_KEY n'est pas définie.")

    resolved_model = model_name or os.getenv("GEMINI_EMBEDDING_MODEL", "gemini-embedding-001")
    return GoogleGenerativeAIEmbeddings(model=resolved_model, google_api_key=api_key)