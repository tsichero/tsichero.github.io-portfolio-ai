# RAG Lab — Evidence

## Smoke test

Query: `como RAG recupera contexto?`

Result: retrieval pipeline returned a top similarity score of **0.568** using TF-IDF + cosine similarity over the local documents.

## Why this is useful

The first version isolates retrieval from generation. That makes the retrieval behavior inspectable before introducing an LLM.

## Next experiment

Add a small evaluation set with expected source documents, then compare lexical retrieval against embedding-based retrieval.
