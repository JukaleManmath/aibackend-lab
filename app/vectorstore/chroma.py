import os
from chromadb import Client
from chromadb.config import Settings

# define the dirc

CHROMA_DB_DIR = "app/vectorstore/chroma_db"

# make sure the directory exists
os.makedirs(CHROMA_DB_DIR, exist_ok=True)

# Initialize the chroma client
chroma_client = Client(Settings(
    persist_directory = CHROMA_DB_DIR,
    anonymized_telemetry = False
))

# collection name
COLLECTION_NAME = "logs_rag"

# get or create the collection
def get_logs_collection():
    return chroma_client.get_or_create_collection(name=COLLECTION_NAME)
