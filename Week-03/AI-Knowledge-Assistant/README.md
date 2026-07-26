# AI Knowledge Assistant

An AI-powered document question-answering system built using Python, FastAPI, ChromaDB, Sentence Transformers, Groq LLMs, JWT authentication, and LangGraph.

The system allows users to upload PDF and TXT documents, process and embed their content, store the embeddings in a vector database, retrieve semantically relevant information, rerank the retrieved documents, and generate answers using an LLM.

## Features

* PDF and TXT document upload
* PDF text extraction
* Text chunking
* Semantic embeddings
* ChromaDB vector database
* Semantic document search
* Document reranking
* Retrieval-Augmented Generation (RAG)
* AI-powered question answering
* Conversation history
* JWT authentication
* FastAPI backend
* LangGraph agent workflow
* Source citation support
* Error handling
* Automated tests using pytest

## System Architecture

```text
User
 │
 ▼
FastAPI API
 │
 ├── Login
 │    └── JWT Authentication
 │
 ├── Upload Document
 │    ├── PDF/TXT Validation
 │    ├── Text Extraction
 │    ├── Text Chunking
 │    ├── Embedding Generation
 │    └── ChromaDB Storage
 │
 └── Ask Question
      │
      ▼
   LangGraph Agent
      │
      ├── Retrieve Documents
      │
      ├── Rerank Documents
      │
      └── Generate Answer
           │
           ▼
        Groq LLM
           │
           ▼
        Answer + Sources
```

## Project Structure

```text
AI-Knowledge-Assistant/
│
├── api/
│   ├── __init__.py
│   ├── auth.py
│   └── main.py
│
├── agents/
│   ├── __init__.py
│   ├── graph.py
│   ├── nodes.py
│   └── state.py
│
├── rag/
│   ├── __init__.py
│   ├── document_processor.py
│   ├── embeddings.py
│   ├── generator.py
│   ├── pipeline.py
│   ├── reranker.py
│   └── retriever.py
│
├── vector_db/
│   ├── __init__.py
│   ├── chroma_store.py
│   └── chroma_data/
│
├── tests/
│   ├── test_agent.py
│   ├── test_api.py
│   ├── test_document_processor.py
│   └── test_pipeline.py
│
├── data/
│   └── ai.txt
│
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```

## Technologies Used

* Python
* FastAPI
* Uvicorn
* Groq API
* Llama 3.1
* Sentence Transformers
* ChromaDB
* PyMuPDF
* LangGraph
* PyJWT
* pytest

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd AI-Knowledge-Assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
JWT_SECRET_KEY=your_secret_key
```

The `.env` file should never be committed to GitHub.

## Running the API

Start the FastAPI server:

```bash
uvicorn api.main:app --reload --port 8001
```

The API will be available at:

```text
http://127.0.0.1:8001
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8001/docs
```

## Authentication

The API uses JWT-based authentication.

### Login

Endpoint:

```text
POST /login
```

Request:

```json
{
    "username":"admin",
    "password":"admin123"
}
```

Response:

```json
{
    "access_token":"your_token",
    "token_type":"bearer"
}
```

The returned token must be included when accessing protected endpoints:

```text
Authorization: Bearer <access_token>
```

## Uploading Documents

Endpoint:

```text
POST /upload
```

Supported file formats:

* PDF
* TXT

The document processing pipeline performs the following steps:

```text
Uploaded File
     │
     ▼
Text Extraction
     │
     ▼
Text Chunking
     │
     ▼
Embedding Generation
     │
     ▼
ChromaDB
```

Each document is split into smaller chunks and converted into vector embeddings.

## Asking Questions

Endpoint:

```text
POST /ask
```

Request:

```json
{
    "question":"What is artificial intelligence?"
}
```

The question passes through the RAG agent workflow:

```text
Question
   │
   ▼
Retrieve Relevant Documents
   │
   ▼
Rerank Documents
   │
   ▼
Generate Context
   │
   ▼
Groq LLM
   │
   ▼
Answer + Sources
```

Example response:

```json
{
    "question":"What is artificial intelligence?",
    "answer":"Artificial Intelligence is a branch of computer science that focuses on creating systems capable of performing tasks that normally require human intelligence.",
    "sources":[
        {
            "source":"ai.txt",
            "page":"None",
            "chunk_id":"ai.txt_None_0",
            "relevant_text":"Artificial Intelligence is a branch of computer science..."
        }
    ]
}
```

## RAG Pipeline

The Retrieval-Augmented Generation pipeline consists of:

### 1. Document Processing

PDF and TXT files are processed and converted into text.

### 2. Chunking

Large documents are divided into smaller text chunks to improve retrieval quality.

### 3. Embedding Generation

Each chunk is converted into a numerical vector representation using a Sentence Transformer model.

### 4. Vector Storage

The embeddings are stored in ChromaDB.

### 5. Semantic Retrieval

When a user asks a question, the question is converted into an embedding and compared against stored document embeddings.

### 6. Reranking

The most relevant retrieved documents are reranked to improve the quality of the context provided to the LLM.

### 7. Answer Generation

The selected document chunks are passed as context to the Groq LLM.

The LLM generates an answer based only on the retrieved document context.

## LangGraph Agent Workflow

The project uses LangGraph to orchestrate the AI workflow.

```text
START
  │
  ▼
Retrieve Node
  │
  ▼
Rerank Node
  │
  ▼
Generate Node
  │
  ▼
END
```

### Retrieve Node

Retrieves the most semantically relevant documents from ChromaDB.

### Rerank Node

Ranks the retrieved documents according to their relevance to the question.

### Generate Node

Generates the final answer using the retrieved context and the Groq LLM.

## Conversation History

The assistant maintains conversation history during the running application.

Previous messages are passed to the LLM so that the assistant can maintain conversational context.

## Source Citations

The system returns information about the document sources used to generate an answer.

Example:

```json
{
    "source":"ai.txt",
    "page":"None",
    "chunk_id":"ai.txt_None_0",
    "relevant_text":"Relevant document content..."
}
```

This allows users to identify which document content was used to answer their question.

## Error Handling

The API handles:

* Invalid login credentials
* Missing authentication tokens
* Invalid or expired JWT tokens
* Unsupported file formats
* Invalid API requests
* Internal processing errors

Examples of HTTP responses:

```text
400 Bad Request
401 Unauthorized
500 Internal Server Error
```

## Testing

The project uses pytest for automated testing.

Run all tests from the project root:

```bash
pytest
```

Current test coverage includes:

* API home endpoint
* Invalid file upload validation
* Document text extraction
* Text chunking
* RAG pipeline
* LangGraph agent workflow

Example test result:

```text
6 passed
```

## Security

The project uses JWT authentication for protected endpoints.

Sensitive credentials are stored in environment variables.

The following files and directories should not be committed:

```text
.env
vector_db/chroma_data/
__pycache__/
.pytest_cache/
```

## Future Improvements

Possible future improvements include:

* User-specific authentication
* Multiple user accounts
* Improved source highlighting
* Streaming LLM responses
* Chat session management
* Conversation persistence
* Improved document metadata handling
* Support for additional file formats
* Advanced reranking models
* Better citation formatting
* Frontend interface
* Role-based access control
* Production deployment

## Project Status

The project currently implements:

* Document upload
* PDF/TXT processing
* Text chunking
* Embedding generation
* ChromaDB vector storage
* Semantic search
* Document reranking
* RAG-based question answering
* Conversation history
* JWT authentication
* LangGraph agent workflow
* FastAPI API
* Source citations
* Automated testing

All implemented tests currently pass successfully.

## Author

Minahil Mobin

AI/ML and Generative AI Engineering Project
