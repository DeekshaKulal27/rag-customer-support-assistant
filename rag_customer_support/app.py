import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

from workflow import detect_intent, escalation_needed
from analytics import init_metrics, add_query, add_escalation
from utils import format_prompt

st.set_page_config(
    page_title="AI Customer Support Copilot",
    layout="wide"
)

# Metrics
init_metrics()

# Sidebar
st.sidebar.title("📊 Analytics Dashboard")
st.sidebar.metric("Total Queries", st.session_state.queries)
st.sidebar.metric("Escalations", st.session_state.escalations)
st.sidebar.markdown("---")
st.sidebar.success("Knowledge Base Loaded")
st.sidebar.write("Model: Llama3 (Local)")
st.sidebar.write("Vector DB: ChromaDB")

# Title
st.title("🤖 AI Customer Support Copilot")
st.caption("RAG + Routing + HITL + Analytics")

# Load System
@st.cache_resource
def load_system():
    embedding = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = Chroma(
        collection_name="support_docs",
        persist_directory="./chroma_db",
        embedding_function=embedding
    )

    llm = Ollama(model="llama3")

    return db, llm

db, llm = load_system()

# Chat Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
query = st.chat_input("Ask support question...")

if query:
    add_query()

    st.session_state.messages.append(
        {"role": "user", "content": query}
    )

    with st.chat_message("user"):
        st.write(query)

    docs = db.similarity_search(query, k=2)
    intent = detect_intent(query)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    if escalation_needed(query, docs):
        add_escalation()

        response = """
This issue needs human attention.
Your request has been escalated to our support team.
"""
    else:
        prompt = format_prompt(
            context,
            query,
            intent
        )

        response = llm.invoke(prompt)

    with st.chat_message("assistant"):
        st.write(response)

        st.info(f"Detected Intent: {intent}")
        st.success("Source: Support Policy KB")

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

# Footer
st.markdown("---")
st.caption("Built by Deeksha | Innomatics Final Project")