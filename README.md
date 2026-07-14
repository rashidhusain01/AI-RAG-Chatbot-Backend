# 🤖 AI RAG Chatbot

An AI-powered Retrieval Augmented Generation (RAG) chatbot that allows users to upload PDF documents and ask questions based on the uploaded content.

The system extracts text from PDFs, creates embeddings, stores them in a FAISS vector database, retrieves relevant information using semantic search, and generates accurate answers using an LLM.

---

## 🚀 Features

- Upload PDF documents
- Extract text from PDF files
- Split documents into smaller chunks
- Generate AI embeddings
- Store embeddings using FAISS vector database
- Semantic search for relevant information
- AI-generated answers using GPT-4o-mini
- FastAPI backend API
- Secure API key management using environment variables

---

## 🛠️ Tech Stack

### Backend

- Python
- FastAPI
- FAISS
- PyMuPDF
- Sentence Transformers
- OpenRouter API
- GPT-4o-mini

### Libraries & Tools

- Uvicorn
- Requests
- Python-dotenv
- Pydantic

---

## 📂 Project Structure

```
AI-RAG-Chatbot/
│
├── app.py                 # FastAPI application
├── embeddings.py          # Text embedding generation
├── llm.py                 # LLM API integration
├── pdf_utils.py           # PDF text extraction & chunking
├── vector_store.py        # FAISS vector database handling
│
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables
├── .gitignore
│
└── uploads/               # Uploaded PDF files
```

---

## ⚙️ How to Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/rashidhusain01/AI-RAG-Chatbot.git
```

### 2. Navigate to Project Folder

```bash
cd AI-RAG-Chatbot
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

### 5. Start Backend Server

```bash
uvicorn app:app --reload
```

Server will run at:

```
http://localhost:8000
```

---

## 📌 API Endpoints

### Health Check

```
GET /health
```

### Upload PDF

```
POST /upload
```

### Ask Questions From Document

```
POST /chat
```

Example:

```json
{
  "question": "What are my technical skills?"
}
```

---

## 🔮 Future Improvements

- React frontend integration
- Modern chatbot UI
- Multiple PDF support
- User authentication
- Chat history storage
- Cloud deployment
- Better document management

---

## 👨‍💻 Author

**Rashid Husain**

Computer Science Engineer  
MERN Stack Developer | AI/RAG Developer