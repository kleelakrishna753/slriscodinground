import faiss
import numpy as np

class FAISSVectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, embeddings, texts):
        self.index.add(np.array(embeddings).astype("float32"))
        self.texts.extend(texts)

    def search(self, query_embedding, top_k):
        D, I = self.index.search(np.array([query_embedding]).astype("float32"), top_k)
        return [self.texts[i] for i in I[0] if i < len(self.texts)]
