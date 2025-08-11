# Research Paper Q&A RAG System - Core Logic Implementation

## Task Overview
Implement a complete RAG pipeline that answers natural language research questions using academic papers as evidence. The infrastructure is ready: your job is to develop the logic for loading, processing, chunking, embedding, storing, searching, and generating answers from research documents.

## Guidance
- Source or create a set of academic papers or excerpts and place them in `data/documents/`.
- Build a document loader, preprocessor, and chunker supporting overlap for optimal retrieval.
- Design and apply an embedding approach suitable for scientific text, ensuring chunk vectors and metadata (title, author, year, paper_id, section) are stored in Chroma.
- Implement vector similarity search with your choice of metric (cosine or dot product) and optimize batch retrieval with top-k queries and basic filtering.
- Wire query encoding, retrieval, and context assembly to a basic natural language generation function to produce scholarly answers referencing relevant sections.
- Evaluate the pipeline with provided example queries and refine for relevance, recall, and answer quality.
- You have complete freedom of models, libraries, and chunking/embedding/search strategies used.

## Database Access Information
- Connect to Chroma DB at `http://<DROPLET_IP>:8000` from your Python code.
- You must define the vector collection(s), dimension, metric, and relevant metadata schema for paper search.
- After embedding ingestion, test and verify chunks and metadata are correctly retrievable using search tools or the Chroma API.

## Objectives
- Ingest and organize research paper content with necessary metadata for later retrieval.
- Implement overlapping chunking and efficient academic text preprocessing.
- Generate and persist high-quality semantic embeddings for chunked content.
- Build a top-k vector search function supporting batch operations and simple metadata filtering.
- Integrate query encoding and retrieval with basic context builder and answer generation.
- Validate end-to-end responses on example queries, confirming evidence grounding and citation correctness.

## How To Verify
- Run test queries from `sample_queries.txt` and confirm retrieved chunks match expected sections.
- Check Chroma DB to ensure chunks and metadata can be retrieved and match paper context.
- Ensure answer generation cites correct paper sections and directly addresses the research question.
- Evaluate precision@k and recall@k for at least one test query, and adjust pipeline if low.
