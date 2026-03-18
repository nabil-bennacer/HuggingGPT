import os
import sys
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_classic.chains import RetrievalQA

sys.path.append(str(Path(__file__).parent.parent / "1-basics"))
from gemini import llm

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY est manquante dans les variables d'environnement.")

loader = PyPDFLoader("foot.pdf")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = text_splitter.split_documents(data)

embedding_model = os.getenv("GEMINI_EMBEDDING_MODEL", "gemini-embedding-001")
embeddings = GoogleGenerativeAIEmbeddings(
    model=embedding_model,
    google_api_key=api_key,
)
vector_db = Chroma.from_documents(documents=chunks, embedding=embeddings)


qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_db.as_retriever()
)

query = "Give me a summary of the document?"
result = qa_chain.invoke(query)

print(f"Analysis Result: {result['result']}")