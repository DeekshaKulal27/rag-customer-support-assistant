from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load text file
loader = TextLoader("knowledge_base/support_policy.txt")
docs = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)

# Embedding model
embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Store in ChromaDB
db = Chroma.from_documents(
    chunks,
    embedding,
    persist_directory="chroma_db"
)

print("Knowledge base stored successfully!")