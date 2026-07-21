import os

from groq import Groq
from dotenv import load_dotenv

from rag.retriever import retrieve_documents
from rag.reranker import rerank_documents

load_dotenv()

client=Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)

conversation_history=[]

def ask_question(
    question
):

    retrieved_documents=retrieve_documents(
        question,
        top_k=5
    )

    ranked_documents=rerank_documents(
        question,
        retrieved_documents,
        top_k=3
    )

    context="\n\n".join(
        document["text"]
        for document in ranked_documents
    )

    history="\n".join(
        f"{message['role']}: {message['content']}"
        for message in conversation_history[-6:]
    )

    prompt=f"""
You are an AI Knowledge Assistant.

Answer the question using only the provided context and conversation history.

If the answer is not available in the provided context, say:
"I do not have enough information in the provided documents."

Conversation History:
{history}

Context:
{context}

Question:
{question}

Answer:
"""

    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        temperature=0.2
    )

    answer=response.choices[0].message.content

    conversation_history.append(
        {
            "role":"user",
            "content":question
        }
    )

    conversation_history.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

    sources=[]

    seen_sources=set()

    for document in ranked_documents:

        source=document["metadata"].get(
            "source"
        )

        page=document["metadata"].get(
            "page"
        )

        source_key=(
            source,
            page
        )

        if source_key not in seen_sources:

            sources.append(
                {
                    "source":source,
                    "page":page
                }
            )

            seen_sources.add(
                source_key
            )

    return {
        "question":question,
        "answer":answer,
        "sources":sources,
        "conversation_history":conversation_history
    }