from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# 1. Load the PDF
loader = PyPDFLoader("Essay Introduction to Belgium - Farah MAHMOUD.pdf")
pages = loader.load()

# 2. Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(pages)
print(f"✅ Loaded and split into {len(chunks)} chunks.")

# 3. Create embeddings
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 4. Store embeddings in ChromaDB
Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_store"
)
print("✅ Embeddings stored locally in ChromaDB ('chroma_store/').")


