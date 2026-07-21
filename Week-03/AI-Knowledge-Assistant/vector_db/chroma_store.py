import chromadb
from rag.embeddings import embedding_model

client=chromadb.PersistentClient(
    path="vector_db/chroma_data"
)

collection=client.get_or_create_collection(
    name="knowledge_base"
)

def add_documents(chunks,embeddings):

    ids=[
        chunk["metadata"]["chunk_id"]
        for chunk in chunks
    ]

    documents=[
        chunk["text"]
        for chunk in chunks
    ]

    metadatas=[
        {
            "source":str(
                chunk["metadata"].get(
                    "source",
                    ""
                )
            ),
            "page":str(
                chunk["metadata"].get(
                    "page",
                    ""
                )
            ),
            "chunk_id":str(
                chunk["metadata"].get(
                    "chunk_id",
                    ""
                )
            )
        }
        for chunk in chunks
    ]

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

def search_documents(
    question,
    top_k=5
):

    document_count=collection.count()

    if document_count==0:

        return []

    question_embedding=embedding_model.encode(
        [question]
    )

    results=collection.query(
        query_embeddings=question_embedding.tolist(),
        n_results=min(
            top_k,
            document_count
        ),
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    if not results["documents"]:

        return []

    if not results["documents"][0]:

        return []

    documents=[]

    for i in range(
        len(
            results["documents"][0]
        )
    ):

        documents.append(
            {
                "text":results["documents"][0][i],
                "metadata":results["metadatas"][0][i],
                "distance":results["distances"][0][i]
            }
        )

    return documents