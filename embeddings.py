from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):

   embeddings = model.encode(chunks)
   embeddings = np.array(embeddings).astype("float32")
   return embeddings


def create_query_embedding(question):

    embedding = model.encode([question])

    embedding = np.array(embedding).astype("float32")

    return embedding