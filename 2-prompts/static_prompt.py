import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "1-basics"))
from gemini import client, MODEL_ID

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