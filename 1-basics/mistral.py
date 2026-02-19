import os

from mistralai import Mistral     
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ["MISTRAL_API_KEY"]

llm_mistral = Mistral(
    api_key = api_key,
)
