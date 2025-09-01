import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama

# Load embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load vector store
vectorstore = Chroma(
    persist_directory="chroma_store",
    embedding_function=embedding_model
)

# Load the LLM
llm = Ollama(model="mistral")

# App title and description
st.title("🔍 Ask My Document")
st.write("Type a question, and I’ll find the most relevant part of the PDF.")

# Form with Ask and Clear buttons
with st.form(key="ask_form"):
    query = st.text_input("Your question:", key="query_input")
    col1, col2 = st.columns([1, 1])
    ask_button = col1.form_submit_button("🧠 Ask")
    clear_button = col2.form_submit_button("❌ Clear")

# Handle Clear
if clear_button:
    st.rerun()

# Handle Ask
if ask_button and query.strip():
    try:
        results = vectorstore.similarity_search(query, k=3)
        if results:
            context = "\n\n".join([doc.page_content for doc in results])

            prompt = f"""Use the context below to answer the user's question.

Context:
{context}

Question: {query}
Answer:"""

            with st.spinner("Thinking..."):
                answer = llm.invoke(prompt)

            st.markdown("### 💡 Answer:")
            st.write(answer)
        else:
            st.warning("No matching content found in the document.")
    except Exception as e:
        st.error(f"Something went wrong: {e}")
