import pickle
import faiss
import os


index = None


FAISS_FILE = "faiss_index.index"
CHUNKS_FILE = "chunks.pkl"



def create_faiss_index(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index



def save_faiss(index, chunks):

    faiss.write_index(
        index,
        FAISS_FILE
    )


    with open(CHUNKS_FILE,"wb") as f:
        pickle.dump(chunks,f)



def load_faiss_data():

    global index


    if not os.path.exists(FAISS_FILE):
        raise Exception("FAISS index not found. Upload PDF first.")


    if index is None:
        index = faiss.read_index(FAISS_FILE)


    with open(CHUNKS_FILE,"rb") as f:
        chunks = pickle.load(f)


    return chunks



def search_faiss(question_embedding, chunks, top_k=3):

    if index is None:
        raise Exception("FAISS index not loaded")


    distance, indices = index.search(
        question_embedding,
        top_k
    )


    results = []


    for i in indices[0]:

        if i != -1:
            results.append(chunks[i])


    return results