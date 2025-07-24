---
#YoutubeLink for Demo video:
##https://youtu.be/nEqX6fj7t3U
---
---

# 🧠 Agentic RAG Chatbot (with MCP)

A modular Retrieval-Augmented Generation (RAG) chatbot that supports multi-format document QA using agent-based architecture and REST-style Model Context Protocol (MCP) message passing.

## 🏗️ Architecture

This system uses 3 primary agents:
- **IngestionAgent**: Parses and preprocesses PDF, DOCX, TXT files.
- **RetrievalAgent**: Generates embeddings and performs semantic retrieval using FAISS.
- **LLMResponseAgent**: Uses OpenAI’s Chat API to respond using contextual chunks.

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
git clone https://github.com/kleelakrishna753/slriscodinground.git
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

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/36a89577-7bed-4777-b350-12a611bd157b" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7fe4176a-494c-4b60-b447-cd693df25d66" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/92d4a7a7-ae57-45b1-8704-39c89c91b81b" />



---

## ✅ Working Example

Uploaded: Management Quarterly Update Fiscal Year 2025 Quarter 2 Update from IRS, and asked:
> “What is the Total Appropriated funds?”

it fetches the precise number with awarness of the context that all numbers are in millions.

You'll get a precise, context-aware answer with extracted evidence.

---

## 📌 TODO / Improvements

* Add memory buffer for multi-turn chat
* Integrate file-based chunk caching
* Add authentication or user-specific namespaces

---

## 🧪 Testing

You can test using public PDFs like:

* https://www.irs.gov/about-irs/irs-financial-reports

---

