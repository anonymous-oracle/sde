# agent.py — line-by-line analysis

## Lines 1-8
- Module docstring, imports logging/os/typing, LangChain agent classes.

## Lines 9-16
- Imports ChatOpenAI, prompts, agent executor, and extract_web_text tool.

## Lines 17-24
- Defines _create_llm and selects MiniMax when API key present.

## Lines 25-32
- Uses OpenAI fallback and starts Agent class init.

## Lines 33-40
- Initializes agent name, tools list, and LLM instance.

## Lines 41-48
- Defines system prompt with translation rules and URL handling.

## Lines 49-56
- Continues system prompt with format requirements and creates prompt template.

## Lines 57-64
- Builds ChatPromptTemplate and creates tool-calling agent/executor.

## Lines 65-72
- process_message logs input and invokes agent executor.

## Lines 73-76
- Returns output text from agent executor result.
