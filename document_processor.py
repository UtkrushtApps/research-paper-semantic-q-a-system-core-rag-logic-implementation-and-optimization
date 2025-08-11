from typing import List, Dict

def load_academic_documents(document_dir: str) -> List[Dict[str, str]]:
    """
    Load all research paper texts and metadata from directory.
    Args:
        document_dir: Directory of academic documents.
    Returns:
        List of dicts with keys like 'title', 'authors', 'year', 'text', etc.
    """
    pass

def preprocess_text(text: str) -> str:
    """
    Basic cleaning and normalization for academic documents.
    Args:
        text: Raw text.
    Returns:
        Preprocessed text.
    """
    pass

def chunk_text(text: str, overlap: int = 50) -> List[str]:
    """
    Split the text into overlapping chunks.
    Args:
        text: Preprocessed academic text.
        overlap: Number of overlapping characters or words.
    Returns:
        List of chunk strings.
    """
    pass
