import streamlit as st
import uuid
from agents.coordinator_agent import bus, register_agents
from mcp.schema import build_mcp_message

st.set_page_config(layout="wide")
st.title("📄 Agentic RAG Chatbot (FAISS + OpenAI + MCP)")

register_agents()

uploaded_file = st.file_uploader("Upload a document (PDF, DOCX, CSV)", type=["pdf", "docx", "csv"])
query = st.text_input("Ask a question about the document")

if st.button("Submit") and uploaded_file and query:
    trace_id = str(uuid.uuid4())

    ingestion_msg = build_mcp_message(
        "UI", "IngestionAgent", "START_INGESTION", trace_id,
        {"file": uploaded_file, "query": query}
    )
    retrieved = bus.send(ingestion_msg)
    retrieved = bus.send(retrieved)  # RetrievalAgent
    final = bus.send(retrieved)      # LLMResponseAgent
    final = bus.send(final)          # CoordinatorAgent

    st.subheader("Answer")
    st.markdown(final["payload"]["answer"])
    with st.expander("Context Chunks"):
        for i, c in enumerate(final["payload"]["chunks"]):
            st.markdown(f"**Chunk {i+1}**:\n{c}")
