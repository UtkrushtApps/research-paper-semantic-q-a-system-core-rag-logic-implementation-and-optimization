from typing import Any, Dict, Optional

class ChromaDBClient:
    """Client utility for Chroma vector database interactions."""
    def __init__(self, host: str, port: int, protocol: str = "http") -> None:
        pass
    def create_collection(self, collection_name: str, dimension: int, metric: str = "cosine", metadata: Optional[Dict[str, Any]] = None) -> Any:
        pass
    def insert_embeddings(self, collection_name: str, embeddings: Any, metadatas: Any) -> None:
        pass
    def search(self, collection_name: str, query_embedding: Any, top_k: int = 5, filter: Optional[Dict[str, Any]] = None) -> Any:
        pass
