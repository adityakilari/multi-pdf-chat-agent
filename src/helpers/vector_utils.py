import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.appconfig import CHROMA_DB_DIR, OLLAMA_MODEL
from langchain_community.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma

def get_vector_store(chunks):
    embeddings = OllamaEmbeddings(model=OLLAMA_MODEL)
    store = Chroma.from_texts(texts=chunks, embedding=embeddings, persist_directory=CHROMA_DB_DIR)
    store.persist()

def load_vector_store():
    embeddings = OllamaEmbeddings(model=OLLAMA_MODEL)
    return Chroma(persist_directory=CHROMA_DB_DIR, embedding_function=embeddings)
