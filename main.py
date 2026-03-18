from embedding import get_gemini_embeddings
from vectorstore import create_gemini_vectorstore
from gemini import get_gemini_chat_model
from langchain.chains import RetrievalQA


llm = get_gemini_chat_model()

texts = 0

embeddings = get_gemini_embeddings()

vectorstore = create_gemini_vectorstore(texts, embeddings)


retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    return_source_documents=True
)

question = "Quel est l'avantage d'une base de données vectorielle ?"
result = qa_chain.invoke({"query": question})

print(f"Réponse : {result['result']}")