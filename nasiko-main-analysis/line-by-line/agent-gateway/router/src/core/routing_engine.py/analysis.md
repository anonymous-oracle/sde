# routing_engine.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports json/logging/typing plus numpy.

## Lines 9-16
- Imports LangChain messages/prompts/documents/embeddings/FAISS.

## Lines 17-24
- Imports settings/RouterOutput, initializes logger, and defines error class.

## Lines 25-32
- Defines RoutingEngine and initializes LLM and embedding model.

## Lines 33-40
- Starts _create_llm docstring and explains provider options.

## Lines 41-48
- Reads provider/model and configures MiniMax ChatOpenAI settings.

## Lines 49-56
- Configures OpenRouter ChatOpenAI or default OpenAI fallback.

## Lines 57-64
- Completes fallback and starts _create_embedding_model.

## Lines 65-72
- Creates OpenAIEmbeddings with reranking model and API key.

## Lines 73-80
- Starts route_query signature and documents inputs/outputs.

## Lines 81-88
- Continues docstring and begins route_query try block.

## Lines 89-96
- Handles small agent list by using all agents and defaults.

## Lines 97-104
- Otherwise runs semantic search with reranking for shortlists.

## Lines 105-112
- Runs LLM routing and returns shortlist/score/router_output.

## Lines 113-120
- Handles routing exceptions and raises RoutingEngineError.

## Lines 121-128
- Defines _prepare_conversation_history string builder.

## Lines 129-136
- Defines cosine similarity helper using numpy operations.

## Lines 137-144
- Starts _rerank_agents signature and docstring.

## Lines 145-152
- Continues docstring, prepares query, and embeds conversation history.

## Lines 153-160
- Computes cosine similarity scores for each embedding.

## Lines 161-168
- Sorts scores and builds second shortlist of agent names.

## Lines 169-176
- Returns second shortlist and starts semantic search method.

## Lines 177-184
- Starts _semantic_search_with_reranking docstring and args.

## Lines 185-192
- Continues docstring and sets k for search results.

## Lines 193-200
- Embeds query and searches FAISS index for distances/indices.

## Lines 201-208
- Initializes search result lists and iterates FAISS indices.

## Lines 209-216
- Retrieves docs and reconstructs embeddings from index.

## Lines 217-224
- Converts L2 distance to cosine similarity and records scores.

## Lines 225-232
- Handles low similarity by using all agents or first shortlist.

## Lines 233-240
- Builds second shortlist using history rerank or top results.

## Lines 241-248
- Filters agent_cards to shortlisted ones.

## Lines 249-256
- Returns shortlists/scores and handles semantic search errors.

## Lines 257-264
- Starts _llm_route signature and docstring.

## Lines 265-272
- Continues docstring and builds system/user prompts.

## Lines 273-280
- Builds ChatPromptTemplate and serializes agent cards JSON.

## Lines 281-288
- Invokes prompt with message/history/cards.

## Lines 289-296
- Calls LLM, validates RouterOutput type, logs selection.

## Lines 297-304
- Returns RouterOutput or logs errors and raises RoutingEngineError.

## Lines 305-312
- Starts router convenience function and docstring.

## Lines 313-320
- Continues docstring and defines arguments/returns.

## Lines 321-328
- Creates RoutingEngine and calls route_query.

## Lines 329-336
- Returns routing results and ends helper.

## Lines 337-344
- End of file.

## Lines 345-346
- End of file.
