from rag.search import semantic_search
from rag.reranker import rerank_documents
from rag.generator import generate_answer
from app.conversation import conversation_history

questions=[
    "What is artificial intelligence?",
    "What are some fields where it is used?",
    "What does it learn from?"
]

for query in questions:
    results=semantic_search(
        query,
        top_k=5
    )

    reranked_results=rerank_documents(
        query,
        results,
        top_k=3
    )

    answer=generate_answer(
        query,
        reranked_results,
        conversation_history
    )

    print("\nQuestion:",query)
    print("\nAnswer:",answer)

print("\nConversation History:")

for message in conversation_history:
    print(message)