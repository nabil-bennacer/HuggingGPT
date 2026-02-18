import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
MODEL_ID = "gemini-2.5-flash"

if __name__ == "__main__":
    print("Chat bot activé (tapez 'quit' ou 'bye' pour sortir)")

    while True:
        prompt = input("\n => Prompt : ").strip().lower()

        if prompt in ["quit", "bye"]:
            print("Au revoir !")
            break

        try:
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=prompt
            )
            print(f"Réponse : {response.text}")
            print(f"Tokens totaux utilisés : {response.usage_metadata.total_token_count}")

        except Exception as e:
            print(f"Erreur : {e}")