import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client=Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_answer(query,documents,conversation_history):
    context="\n\n".join(
        document["text"]
        for document in documents
    )

    messages=[
        {
            "role":"system",
            "content":"Answer questions using the provided document context. If the answer is not present in the context, say that the information was not found in the provided documents."
        }
    ]

    for message in conversation_history:
        messages.append(message)

    messages.append(
        {
            "role":"user",
            "content":f"""
Context:
{context}

Question:
{query}
"""
        }
    )

    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0
    )

    answer=response.choices[0].message.content

    conversation_history.append(
        {
            "role":"user",
            "content":query
        }
    )

    conversation_history.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

    return answer