from sentence_transformers import SentenceTransformer
from app.vectorstore.chroma import get_logs_collection
from uuid import uuid4

model = SentenceTransformer("all-MiniLm-L6-v2")

collection = get_logs_collection()

def get_embedding(text: str) -> list[float]:
    return model.encode(text).tolist()

def add_log_to_chroma(raw_log: str, summary: str) -> str:
    text_to_embed = raw_log.strip()
    embedding = model.encode(text_to_embed).tolist()
    doc_id = str(uuid4())
    collection.add(
        documents= [text_to_embed],
        embeddings=[embedding],
        metadatas=[{"source": "log_entry",
                    "summary": summary.strip(),
                    "raw_log": raw_log.strip()
                    }],
        ids=[doc_id]
    )
    return doc_id

def query_logs_from_chroma(query: str, n_results: int = 3) -> list[dict[str, str]]:
    collection = get_logs_collection()
    query_embedding = get_embedding(query)

    results= collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    # for my reference hoe the result looks like
    # print(results)
    return [
        {
            "raw_log": doc,
            "summary": meta.get("summary", "No summary")
        }
        for doc, meta in zip(results["documents"][0], results["metadatas"][0])
    ]