from utils.file_loader import load_file
from utils.chunking import chunk_text
from mcp.schema import build_mcp_message

def handle_ingestion(message):
    file = message["payload"]["file"]
    trace_id = message["trace_id"]
    raw_text = load_file(file)
    chunks = chunk_text(raw_text)
    return build_mcp_message(
        "IngestionAgent", "RetrievalAgent", "INGESTION_COMPLETE", trace_id,
        {"chunks": chunks, "query": message["payload"]["query"]}
    )
