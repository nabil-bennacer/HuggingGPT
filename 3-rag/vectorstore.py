from langchain_community.vectorstores import Chroma

def create_gemini_vectorstore(documents, embeddings):
    """
    Crée une base Chroma à partir d'une liste de documents.
    """
    vectorstore = Chroma.from_documents(documents=documents, embedding=embeddings)
    return vectorstore