Great! Here's everything you need:

---

# ✅ `README.md` — Complete Setup & Usage Instructions

````markdown
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

---

# 📊 PPT Presentation — Agentic RAG Chatbot

Here’s the slide deck breakdown you can create using PowerPoint or Google Slides:

---

## ✅ Slide 1: Title Slide

**Title:**  
Agentic RAG Chatbot for Multi-format Document QA

**Subtitle:**  
Modular Agent Architecture + MCP Messaging + Streamlit UI

---

## ✅ Slide 2: Architecture Overview

**Title:** Agent-based RAG Architecture

- IngestionAgent → RetrievalAgent → LLMResponseAgent
- All agents communicate using Model Context Protocol (MCP)
- Coordinated via `Bus` or `CoordinatorAgent`

🧱 Components:
- FAISS
- OpenAI Chat API
- PyMuPDF
- Streamlit

---

## ✅ Slide 3: System Flow Diagram

**Title:** Message Flow (MCP-Based)

Diagram Flow:
```

User ⟶ IngestionAgent ⟶ RetrievalAgent ⟶ LLMResponseAgent ⟶ Streamlit UI
⬇                       ⬇                  ⬇
\[MCP: DOC\_INGEST]     \[MCP: CONTEXT\_REQUEST] \[MCP: ANSWER]

```

---

## ✅ Slide 4: Tech Stack

**Title:** Tech Stack Used

- 🔍 Retrieval: FAISS
- 🤖 Embeddings: OpenAI (`text-embedding-3-small`)
- 🧠 LLM: OpenAI GPT-3.5 / GPT-4
- 📂 Docs: PyMuPDF (PDF), python-docx
- 🧪 UI: Streamlit
- 💬 Comms: REST-style MCP messages

---

## ✅ Slide 5: UI Screenshots

Include:
- Upload screen
- Chat with answer + citation
- Debug trace (optional)

---

## ✅ Slide 6: Challenges & Future Scope

**Title:** Challenges Faced

- OpenAI SDK migration (v1+)
- Handling multi-format parsing
- Consistent message passing via MCP
- Session state across agents

**Future Scope:**
- LangChain agent orchestration
- Asynchronous agent execution
- User-authenticated namespace isolation

---

Would you like a downloadable `.pptx` version as well?  
Or shall I create a ready-made Google Slides deck for you?
```
