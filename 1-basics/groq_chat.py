import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")
model = "llama-3.1-8b-instant"

client = Groq(api_key=api_key)

while True:
    prompt = input("\n=> Enter your prompt : ")

    if prompt.lower() in ["bye", "quit"]:
        print("Au revoir !")
        break

    chat_response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ]
    )

    print(chat_response.choices[0].message.content)
    print("Tokens utilisés :", chat_response.usage.total_tokens)