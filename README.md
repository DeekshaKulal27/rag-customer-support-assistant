# AI Customer Support Copilot

## 🚀 Final Internship Project  
**RAG-Based Customer Support Assistant with Routing, HITL & Analytics**

Built by **Deeksha** for **Innomatics Research Labs Final Evaluation Project**

---

## 📌 Project Overview

AI Customer Support Copilot is an intelligent customer support assistant built using **Retrieval-Augmented Generation (RAG)** architecture.

The system retrieves relevant company policy data from a local knowledge base and uses a local LLM to generate accurate responses.

It also supports:

- Intent Detection
- Human-in-the-Loop (HITL) Escalation
- Analytics Dashboard
- Chat History
- Professional UI

---

## 🧠 Features

### Core AI Features
- RAG-based question answering
- Semantic search using embeddings
- Local LLM integration using Ollama
- ChromaDB vector database

### Workflow Features
- Query intent detection: Refund, Shipping, Cancellation, Exchange, Complaint
- Smart routing logic
- Human escalation for sensitive queries

### UI Features
- Modern chat interface
- Sidebar analytics dashboard
- Chat memory/history
- Source display
- Footer branding

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- Ollama
- Llama3
- Sentence Transformers

---

## 📂 Project Structure

```text
rag_customer_support/
│── app.py
│── ingest.py
│── workflow.py
│── analytics.py
│── utils.py
│── knowledge_base/
│   └── support_policy.txt
│── chroma_db/
│── README.md
```

---

## ⚙️ Installation & Setup

```bash
git clone <your-github-link>
cd rag_customer_support
pip install langchain langgraph chromadb pypdf sentence-transformers langchain-community streamlit
pip install langchain-text-splitters
ollama run llama3
python ingest.py
streamlit run app.py
```

---

## 💬 Sample Queries

- Can I get refund after 7 days?
- How many days shipping takes?
- Can I cancel my order?
- I have legal complaint

---

## 👩‍💻 Author

**Deeksha**  
Final Project Submission for **Innomatics Research Labs**
