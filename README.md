
---

# ✅ `README.md` — Complete Setup & Usage Instructions

# 🧠 Agentic RAG Chatbot (with MCP)

A modular Retrieval-Augmented Generation (RAG) chatbot that supports multi-format document QA using agent-based architecture and REST-style Model Context Protocol (MCP) message passing.

## 🏗️ Architecture

This system uses 3 primary agents:
- **IngestionAgent**: Parses and preprocesses PDF, DOCX, TXT files.
- **RetrievalAgent**: Generates embeddings and performs semantic retrieval using FAISS.
- **LLMResponseAgent**: Uses OpenAI’s Chat API to respond using contextual chunks.
- **(Optional) CoordinatorAgent**: Orchestrates message routing using MCP-style messages.

All communication happens via structured MCP messages like:

```json
{
  "sender": "RetrievalAgent",
  "receiver": "LLMResponseAgent",
  "type": "CONTEXT_RESPONSE",
  "trace_id": "abc-123",
  "payload": {
    "top_chunks": ["..."],
    "query": "What are the KPIs?"
  }
}
````

---

## 🧰 Tech Stack

* 🧠 OpenAI Chat API (gpt-4 / gpt-3.5-turbo)
* 🧲 FAISS vector store
* 📎 PyMuPDF for PDF parsing
* 🖥️ Streamlit UI
* 📡 REST-like internal messaging using MCP format

---

## 🚀 Installation

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/agentic-rag-chatbot.git
cd agentic-rag-chatbot
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set OpenAI API Key**
   Create a `.env` file or set your key in `config.py`:

```python
OPENAI_API_KEY = "your-api-key"
CHAT_MODEL = "gpt-3.5-turbo"
EMBEDDING_MODEL = "text-embedding-3-small"
```

4. **Run the app**

```bash
streamlit run streamlit_app.py
```

---

## 📎 Features

* Multi-format document upload (PDF, DOCX, TXT)
* Semantic search using vector DB (FAISS)
* Modular agent-based processing
* Persistent session context via `trace_id`
* Answer with citations (source chunks)

---

## 📸 Screenshot

![Screenshot](screenshots/app_ui.png)

---

## ✅ Working Example

Upload a sample PDF (e.g. an invoice or report), and ask:

> “What is the total amount due?”

You'll get a precise, context-aware answer with extracted evidence.

---

## 📌 TODO / Improvements

* Add memory buffer for multi-turn chat
* Integrate file-based chunk caching
* Add authentication or user-specific namespaces

---

## 🧪 Testing

You can test using public PDFs like:

* [sample invoice](https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf)

---

## 📄 License

MIT License

```
