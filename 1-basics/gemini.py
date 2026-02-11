import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
prompt = "The quick brown fox jumps over the lazy dog."

MODEL_ID = "gemini-2.5-flash"

try:
    print(f"--- Utilisation de {MODEL_ID} ---")

    # Test de génération
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    )

    print(f"Réponse : {response.text}")
    print(f"Tokens totaux utilisés : {response.usage_metadata.total_token_count}")

except Exception as e:
    print(f"Erreur : {e}")