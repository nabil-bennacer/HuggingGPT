from langchain.vectorstores import FAISS

def create_gemini_vectorstore(texts, embeddings):
    """
    Crée une base FAISS à partir d'une liste de textes.
    """
    vectorstore = FAISS.from_texts(texts, embeddings)
    return vectorstore