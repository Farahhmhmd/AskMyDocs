# 🔍 AskMyDocs

AskMyDocs is a local RAG-based document chatbot built with **LangChain**, **ChromaDB**, and **Streamlit**. It allows you to query your PDF documents and get smart answers powered by a local LLM (Mistral via Ollama).

## 🚀 How It Works

1. `embed_and_store.py`:
   - Loads and splits your PDF.
   - Generates embeddings using `all-MiniLM-L6-v2`.
   - Stores chunks in ChromaDB locally.

2. `app.py`:
   - Loads the vector store and a local LLM (Mistral).
   - Uses LangChain to retrieve relevant chunks and generate an answer.

## 🛠️ Requirements

- Python 3.10+
- Ollama installed with Mistral model
- Virtual environment recommended

## 📦 Setup

```bash
git clone https://github.com/yourusername/AskMyDocs.git
cd AskMyDocs
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```
## ▶️ Run the App

```bash
streamlit run app.py
```

## 📄 Author
Farah Mahmoud - https://www.linkedin.com/in/farahhmahmoudd/
---

