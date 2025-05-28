import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env

# Vector DB
CHROMA_DB_DIR = "chroma_db"

# Model config
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "Mistral")

# Embedding config
EMBEDDING_DIMENSION = int(os.getenv("EMBEDDING_DIMENSION", "4096"))