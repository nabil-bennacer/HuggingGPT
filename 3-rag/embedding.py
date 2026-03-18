import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def get_gemini_embeddings(model_name: str = "models/embedding-001") -> GoogleGenerativeAIEmbeddings:
    
    if "GOOGLE_API_KEY" not in os.environ:
        raise ValueError("La variable d'environnement GOOGLE_API_KEY n'est pas définie.")
    
    return GoogleGenerativeAIEmbeddings(model=model_name)