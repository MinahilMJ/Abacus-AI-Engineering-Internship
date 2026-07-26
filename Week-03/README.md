# Week 3 & 4 AI Engineering Assignments

This repository contains the assignments and final project completed during Week 3–4 of the AI Engineering Internship.

The work focuses on Large Language Models, prompt engineering, embeddings, vector databases, Retrieval-Augmented Generation, AI agents, and FastAPI backend development.

---

## Part 1: LLM API Integration

### AI Chatbot

A chatbot was developed using an LLM API provider.

### Features

* Accepts user input
* Generates AI responses
* Maintains conversation history
* Handles API errors
* Stores chat history in JSON format

The chatbot demonstrates how applications can communicate with Large Language Models through APIs.

---

## Part 2: Prompt Engineering

Prompts were designed for different real-world use cases.

### Use Cases

* Email Generator
* Resume Reviewer
* Code Reviewer
* Customer Support Assistant
* Travel Planner

### Challenge

The assignment also explored the difference between:

### Zero-Shot Prompting

The model receives an instruction without examples.

### Few-Shot Prompting

The model receives examples along with the instruction to guide the expected response.

The prompts were compared and improved to achieve better response quality, accuracy, and consistency.

---

## Part 3: Embeddings and Vector Databases

A semantic search system was developed to search documents based on meaning rather than exact keyword matching.

### Process

1. Load multiple documents
2. Split documents into smaller chunks
3. Generate embeddings for each chunk
4. Store the embeddings in a vector database
5. Convert a user query into an embedding
6. Retrieve the Top-K most semantically similar document chunks

### Technologies

* Python
* Sentence Transformers
* Embeddings
* ChromaDB

This system forms the foundation of the Retrieval-Augmented Generation pipeline.

---

## Part 4: Retrieval-Augmented Generation

A document question-answering system was developed using RAG.

### Process

1. Upload PDF or TXT documents
2. Extract text from the documents
3. Split the text into smaller chunks
4. Generate embeddings
5. Store the embeddings in ChromaDB
6. Retrieve relevant document chunks for a question
7. Rerank the retrieved documents
8. Provide the relevant context to an LLM
9. Generate an answer based on the retrieved documents
10. Display source references

The system is designed to answer questions using information from the uploaded documents instead of relying only on the LLM's general knowledge.

---

## Part 5: AI Agent

A basic AI Agent workflow was implemented using LangGraph.

The agent processes a user question through multiple steps:

```text
User Question
      ↓
Document Retrieval
      ↓
Document Reranking
      ↓
Answer Generation
      ↓
Final Response
```

### Agent Capabilities

* Accepts a user question
* Retrieves relevant document information
* Reranks retrieved documents
* Generates a final response using an LLM
* Returns relevant source references

The workflow demonstrates how multiple AI processing steps can be connected into an agent-like system.

---

## Part 6: API Development

A FastAPI backend was developed to expose the AI system through API endpoints.

### Main Endpoints

### `/chat`

Used for chatbot-style interactions.

### `/upload`

Used to upload PDF and TXT documents.

Uploaded documents are:

* Saved locally
* Processed
* Split into chunks
* Converted into embeddings
* Stored in the vector database

### `/ask`

Used to ask questions about the uploaded documents.

The system:

* Validates the request
* Searches the vector database
* Retrieves relevant content
* Reranks the results
* Generates an answer
* Returns source references

### Additional API Features

* Request validation using Pydantic
* Error handling
* Environment variables
* JWT-based authentication

---

# Final Project: AI Knowledge Assistant

The final project combines the concepts covered throughout the assignments into one complete AI application.

The system allows users to upload documents and ask questions about their content.

## Main Features

* Upload PDF and TXT documents
* Extract text from documents
* Split text into chunks
* Generate embeddings
* Store vectors in ChromaDB
* Perform semantic search
* Retrieve relevant document chunks
* Rerank retrieved documents
* Generate answers using an LLM
* Maintain conversation history
* Display source references
* Provide source highlighting
* Use an AI agent workflow
* Expose functionality through a FastAPI backend
* Handle API errors
* Authenticate users using JWT

---

## RAG Workflow

```text
Upload Document
      ↓
Extract Text
      ↓
Create Chunks
      ↓
Generate Embeddings
      ↓
Store in ChromaDB
      ↓
User Asks Question
      ↓
Semantic Search
      ↓
Retrieve Relevant Chunks
      ↓
Rerank Documents
      ↓
Send Context to LLM
      ↓
Generate Answer
      ↓
Return Sources
```

---

## AI Agent Workflow

The LangGraph workflow connects multiple processing nodes:

```text
START
  ↓
Retrieve Documents
  ↓
Rerank Documents
  ↓
Generate Answer
  ↓
END
```

Each stage performs a specific task in the question-answering process.

---

## Authentication

JWT authentication was added to protect the main API functionality.

The authentication flow is:

```text
User Login
    ↓
Username and Password Verification
    ↓
JWT Token Generated
    ↓
Token Sent with API Request
    ↓
Token Verified
    ↓
Protected Endpoint Accessed
```

Protected endpoints require a valid Bearer token.

---

## Document Reranking

The system first retrieves multiple potentially relevant documents using semantic search.

The retrieved documents are then reranked to identify the most relevant chunks before they are passed to the LLM.

```text
User Question
      ↓
Semantic Search
      ↓
Top-K Documents
      ↓
Reranking
      ↓
Most Relevant Documents
      ↓
LLM Context
```

This helps improve the quality of the final answer.

---

## Source References

The generated responses include information about the source documents used to answer the question.

Example:

```json
{
  "source": "ai.txt",
  "page": "None",
  "chunk_id": "ai.txt_None_0",
  "relevant_text": "Relevant document content..."
}
```

This allows users to identify where the information used in the answer came from.

---

## Testing

Automated tests were written using Pytest.

The tests cover:

* API endpoints
* Invalid file uploads
* Document text extraction
* Text chunking
* AI pipeline functionality
* Agent workflow

The final test suite successfully passed all tests.

---


## Technologies Used

* Python
* FastAPI
* Uvicorn
* Groq API
* Llama 3.1
* Sentence Transformers
* Embeddings
* ChromaDB
* LangGraph
* Pytest
* JWT Authentication


---

## Overall Project Architecture

```text
                    ┌─────────────────┐
                    │     Client      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   FastAPI API   │
                    └────────┬────────┘
                             │
             ┌───────────────┴───────────────┐
             │                               │
             ▼                               ▼
       Upload Documents                 Ask Question
             │                               │
             ▼                               ▼
       Document Processor              AI Agent Workflow
             │                               │
             ▼                               ▼
         Chunking                    Document Retrieval
             │                               │
             ▼                               ▼
        Embeddings                     Reranking
             │                               │
             ▼                               ▼
          ChromaDB                    Relevant Context
                                             │
                                             ▼
                                       LLM Generation
                                             │
                                             ▼
                                       Final Answer
                                             │
                                             ▼
                                      Source References
```

---

## Summary

This project demonstrates the complete workflow of building an AI-powered knowledge assistant.

The project combines:

* LLM API integration
* Prompt engineering
* Embeddings
* Semantic search
* Vector databases
* Retrieval-Augmented Generation
* Document processing
* AI agent workflows
* Document reranking
* Source citations
* JWT authentication
* FastAPI backend development
* Automated testing

The final result is an AI Knowledge Assistant capable of processing documents, searching their content, answering questions using relevant context, and providing source information for the generated answers.
