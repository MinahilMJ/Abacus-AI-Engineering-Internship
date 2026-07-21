from rag.retriever import retrieve_documents
from rag.reranker import rerank_documents
from rag.generator import generate_answer


conversation_history=[]


def retrieve_node(
    state
):

    retrieved_documents=retrieve_documents(
        state["question"],
        top_k=5
    )

    return {
        "retrieved_documents":retrieved_documents
    }


def rerank_node(
    state
):

    ranked_documents=rerank_documents(
        state["question"],
        state["retrieved_documents"],
        top_k=3
    )

    context="\n\n".join(
        document["text"]
        for document in ranked_documents
    )

    return {
        "ranked_documents":ranked_documents,
        "context":context
    }


def generate_node(
    state
):

    answer=generate_answer(
        state["question"],
        state["ranked_documents"],
        conversation_history
    )

    sources=[]

    seen_sources=set()

    for document in state["ranked_documents"]:

        metadata=document.get(
            "metadata",
            {}
        )

        source=metadata.get(
            "source"
        )

        page=metadata.get(
            "page"
        )

        chunk_id=metadata.get(
            "chunk_id"
        )

        text=document.get(
            "text",
            ""
        )

        source_key=(
            source,
            page,
            chunk_id
        )

        if source_key not in seen_sources:

            sources.append(
                {
                    "source":source,
                    "page":page,
                    "chunk_id":chunk_id,
                    "relevant_text":text
                }
            )

            seen_sources.add(
                source_key
            )

    return {
        "answer":answer,
        "sources":sources
    }