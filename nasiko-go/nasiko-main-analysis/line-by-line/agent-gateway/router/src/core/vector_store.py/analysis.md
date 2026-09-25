# vector_store.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports logging/typing plus FAISS/embeddings.

## Lines 9-16
- Imports settings, initializes logger, and defines VectorStoreError.

## Lines 17-24
- Starts VectorStoreService and initializes embeddings/cache fields.

## Lines 25-32
- Defines _create_embeddings and enforces OpenAI API key presence.

## Lines 33-40
- Builds OpenAIEmbeddings instance and starts create_vector_store signature.

## Lines 41-48
- Documents args/returns/errors for create_vector_store.

## Lines 49-56
- Hashes cards and returns cached store if valid.

## Lines 57-64
- Prepares texts/metadatas and errors on missing data.

## Lines 65-72
- Builds FAISS store from texts and updates cache.

## Lines 73-80
- Returns vectorstore or handles exceptions with error logging.

## Lines 81-88
- Defines _prepare_data and starts docstring.

## Lines 89-96
- Initializes text/metadata lists and starts iterating cards.

## Lines 97-104
- Extracts description/name and warns on missing data.

## Lines 105-112
- Appends description/metadata and handles per-card errors.

## Lines 113-120
- Returns prepared texts/metadatas and starts _hash_agent_cards.

## Lines 121-128
- Imports hashlib/json, sorts cards, and dumps JSON.

## Lines 129-136
- Hashes JSON and defines _is_cache_valid logic.

## Lines 137-144
- Returns cache validity and starts similarity_search signature.

## Lines 145-152
- Documents similarity_search args/returns.

## Lines 153-160
- Executes similarity search and builds metadata+score list.

## Lines 161-168
- Logs matches and returns list or handles errors.

## Lines 169-176
- Raises VectorStoreError and defines clear_cache.

## Lines 177-177
- Clears cache and logs completion.
