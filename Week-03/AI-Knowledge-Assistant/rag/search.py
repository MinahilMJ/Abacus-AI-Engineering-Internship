from sentence_transformers import SentenceTransformer
from vector_db.chroma_store import search_documents

embedding_model=SentenceTransformer("all-MiniLM-L6-v2")

def semantic_search(query,top_k=5):
    query_embedding=embedding_model.encode([query])

    results=search_documents(
        query_embedding,
        top_k
    )

    search_results=[]

    for index in range(len(results["documents"][0])):
        search_results.append({
            "text":results["documents"][0][index],
            "metadata":results["metadatas"][0][index],
            "distance":results["distances"][0][index]
        })

    return search_results