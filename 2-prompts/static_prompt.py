
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "1-basics"))

from gemini import llm

prompt = "Quel est le sens de la vie ?"

try:
    response = llm.invoke(prompt)
    
    print(f"Réponse : {response.content}")
    
    tokens = response.response_metadata.get("token_usage", {})
    print(f"Tokens utilisés : {tokens.get('total_tokens', 'N/A')}")

except Exception as e:
    print(f"Erreur : {e}")