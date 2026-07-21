from vector_db.chroma_store import search_documents

def retrieve_documents(question,top_k=5):
    return search_documents(
        question,
        top_k
    )