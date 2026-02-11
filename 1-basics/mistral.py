
import os

from mistralai import Mistral     
from dotenv import load_dotenv

load_dotenv()

# Récupération de la clé API à partir des variables d'environnement
api_key = os.environ["MISTRAL_API_KEY"]
# Définition du modèle à utiliser pour la requête
model = "mistral-small-latest"

# Création d'une instance de la classe Mistral avec la clé API
client = Mistral(api_key=api_key)

# Boucle infinie pour permettre une interaction continue avec l'utilisateur
while True:

    prompt = input("\n=> Enter your prompt : ")


    if prompt in ["bye", "quit"]:
        break  # on quiite le programme

    
    chat_response = client.chat.complete(
        model=model,                   # Spécification du modèle à utiliser
        messages=[                     # Liste des messages pour la conversation
            {
                "role": "user",        # Rôle de l'expéditeur du message (ici, l'utilisateur)
                "content": prompt,     # Contenu du message, basé sur l'entrée de l'utilisateur
            },
        ]
    )

    print(chat_response.choices[0].message.content)
    print("Tokens utilisés :", chat_response.usage.total_tokens)