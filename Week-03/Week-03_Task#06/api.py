import os
import chromadb
from fastapi import FastAPI,UploadFile,File
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

app=FastAPI()

client=Groq(api_key=os.getenv("GROQ_API_KEY"))

embedding_model=SentenceTransformer("all-MiniLM-L6-v2")

chroma_client=chromadb.PersistentClient(path="chroma_db")

collection=chroma_client.get_or_create_collection(
    name="documents"
)

class ChatRequest(BaseModel):
    message:str

class AskRequest(BaseModel):
    question:str

@app.get("/")
def home():
    return {"message":"AI API is running"}

@app.post("/chat")
def chat(request:ChatRequest):
    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role":"user",
                "content":request.message
            }
        ]
    )

    return {
        "user_message":request.message,
        "response":response.choices[0].message.content
    }

@app.post("/upload")
async def upload_file(file:UploadFile=File(...)):
    if not file.filename.endswith((".pdf",".txt")):
        return {"error":"Only PDF and TXT files are allowed"}

    file_content=await file.read()

    with open(file.filename,"wb") as f:
        f.write(file_content)

    return {
        "filename":file.filename,
        "message":"File uploaded successfully"
    }

@app.post("/ask")
def ask(request:AskRequest):
    query_embedding=embedding_model.encode([request.question])

    results=collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=3
    )

    context="\n\n".join(results["documents"][0])
    sources=results["metadatas"][0]

    prompt=f"""
Answer the question using only the provided context.

Context:
{context}

Question:
{request.question}
"""

    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return {
        "question":request.question,
        "answer":response.choices[0].message.content,
        "sources":sources
    }