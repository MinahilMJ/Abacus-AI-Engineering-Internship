from fastapi import FastAPI,UploadFile,File,HTTPException,Depends
from pydantic import BaseModel
import shutil
import os

from agents.graph import ask_agent
from rag.document_processor import extract_text,create_chunks
from rag.embeddings import generate_embeddings
from vector_db.chroma_store import add_documents
from api.auth import create_access_token,get_current_user

app=FastAPI(
    title="AI Knowledge Assistant"
)

UPLOAD_FOLDER="uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


class QuestionRequest(BaseModel):

    question:str


class LoginRequest(BaseModel):

    username:str
    password:str


@app.get("/")
def home():

    return {
        "message":"AI Knowledge Assistant API is running"
    }


@app.post("/login")
def login(
    request:LoginRequest
):

    if request.username!="admin" or request.password!="admin123":

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token=create_access_token(
        request.username
    )

    return {
        "access_token":token,
        "token_type":"bearer"
    }


@app.post("/ask")
def ask(
    request:QuestionRequest,
    current_user=Depends(get_current_user)
):

    try:

        result=ask_agent(
            request.question
        )

        return result

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@app.post("/upload")
async def upload_file(
    file:UploadFile=File(...),
    current_user=Depends(get_current_user)
):

    if not file.filename.lower().endswith(
        (".pdf",".txt")
    ):

        raise HTTPException(
            status_code=400,
            detail="Only PDF and TXT files are allowed"
        )

    file_path=os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    pages=extract_text(
        file_path
    )

    chunks=create_chunks(
        pages,
        file.filename
    )

    embeddings=generate_embeddings(
        chunks
    )

    add_documents(
        chunks,
        embeddings
    )

    return {
        "message":"File uploaded and processed successfully",
        "filename":file.filename,
        "chunks":len(chunks)
    }