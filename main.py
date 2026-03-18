import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR / "3-rag"))
sys.path.append(str(BASE_DIR / "1-basics"))

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains import RetrievalQA
from embedding import get_gemini_embeddings
from vectorstore import create_gemini_vectorstore
from gemini import get_gemini_chat_model

llm = get_gemini_chat_model()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY est manquante dans les variables d'environnement.")

pdf_path = BASE_DIR / "3-PDFLoader" / "foot.pdf"
if not pdf_path.exists():
    raise FileNotFoundError(f"Fichier PDF introuvable: {pdf_path}")

loader = PyPDFLoader(str(pdf_path))
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = text_splitter.split_documents(data)


embeddings = get_gemini_embeddings()

vectorstore = create_gemini_vectorstore(chunks, embeddings)

retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    return_source_documents=True
)

query = "Give me a summary of the document?"
result = qa_chain.invoke(query)

print(f"Analysis Result: {result['result']}")