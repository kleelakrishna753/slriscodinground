from utils.embeddings import get_embedding
from utils.vector_store import FAISSVectorStore
from mcp.schema import build_mcp_message
from config import TOP_K

vector_store = None

def handle_retrieval(message):
    global vector_store
    chunks = message["payload"]["chunks"]
    embeddings = [get_embedding(chunk) for chunk in chunks]
    vector_store = FAISSVectorStore(len(embeddings[0]))
    vector_store.add(embeddings, chunks)

    query = message["payload"]["query"]
    query_embedding = get_embedding(query)
    top_chunks = vector_store.search(query_embedding, TOP_K)

    return build_mcp_message(
        "RetrievalAgent", "LLMResponseAgent", "CONTEXT_RESPONSE", message["trace_id"],
        {"top_chunks": top_chunks, "query": query}
    )
