import sys
from pathlib import Path
from langchain_core.prompts import PromptTemplate

sys.path.append(str(Path(__file__).parent.parent / "1-basics"))
from groq_chat import llm_groq


conversation_history = []

template_beginner = PromptTemplate(
    input_variables = ["topic"],
    template = "Explain in 10 lignes maximum{topic} as I were a beginner and make sure I can understand all the concepts"
)

template_steps = PromptTemplate(
    input_variables = ["topic"],
    template = "Explain in 10 lignes maximum {topic} step by step and make sure I can understand all the concepts"
)

prompt1 = template_beginner.format(topic = "airplane takeoff")
prompt2 = template_steps.format(topic = "airplane takeoff")

response1 = llm_groq.chat.completions.create(messages=[{"role": "user", "content": prompt1}], model="llama-3.1-8b-instant")
response2 = llm_groq.chat.completions.create(messages=[{"role": "user", "content": prompt2}], model="llama-3.1-8b-instant")

conversation_history.append({"prompt": prompt1, "response": response1.choices[0].message.content})
conversation_history.append({"prompt": prompt2, "response": response2.choices[0].message.content})

print("Beginner explanation:")
print(response1.choices[0].message.content)
print("\nStep-by-step explanation:")
print(response2.choices[0].message.content)
# print("\nConversation history:", conversation_history)
