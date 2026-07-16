import os
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile, File, HTTPException
from pdf_utils import extract_text_from_pdf, split_text_into_chunks

from embeddings import create_embeddings, create_query_embedding

from embeddings import get_model


from vector_store import (
    create_faiss_index,
    save_faiss,
    load_faiss_data,
    search_faiss
)


from llm import generate_answer

app = FastAPI()



@app.on_event("startup")
def startup():
    print("Loading embedding model...")
    get_model()
    print("Embedding model loaded successfully.")



app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://ai-rag-chatbot-frontend.vercel.app",
        "https://ai-rag-chatbot-frontend-30xksfspu-rashid-cse.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return{
        "message":"Welcome to RAG Chatbot API"
    }


@app.get("/health")
def health():
   return{
            "status": "Backend Running"
    }  

class QuestionRequest(BaseModel):
   question: str
    

 

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:

        print("1")

        if file.content_type != "application/pdf":
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are allowed."
            )

        print("2")

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        print("3")

        pdf_text = extract_text_from_pdf(file_path)

        if not pdf_text.strip():
            raise HTTPException(
        status_code=400,
        detail="PDF contains no readable text."
        )
        

        print("4")

        chunks = split_text_into_chunks(pdf_text)

        print("Chunks =", len(chunks))

        embeddings = create_embeddings(chunks)

        print("5")

        index = create_faiss_index(embeddings)

        print("6")

        save_faiss(index, chunks)

        print("7")

        return {
            "message": "Success"
        }

    except Exception as e:
        import traceback

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )




@app.post("/search")
def search(request: QuestionRequest):

    try:
        chunks = load_faiss_data()

    except Exception as e:
        return {
            "error": str(e)
        }


    question_embedding = create_query_embedding(
        request.question
    )


    results = search_faiss(
        question_embedding,
        chunks
    )


    return{
        "question": request.question,
        "results": results
    }




@app.post("/chat")
def chat(request: QuestionRequest):

    try:
        chunks = load_faiss_data()

    except Exception as e:
        return {
            "error": str(e)
        }


    question_embedding = create_query_embedding(
        request.question
    )


    results = search_faiss(
        question_embedding,
        chunks
    )


    if not results:
        return {
            "answer":"No relevant information found."
        }


    context = "\n\n".join(results)


    answer = generate_answer(
        context,
        request.question
    )


    return{
        "question": request.question,
        "answer": answer
    }