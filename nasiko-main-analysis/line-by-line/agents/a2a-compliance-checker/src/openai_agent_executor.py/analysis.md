# openai_agent_executor.py — line-by-line analysis

## Lines 1-8
- Imports json/logging/Any and A2A agent execution/context/event types.

## Lines 9-16
- Imports TaskUpdater, A2A types, ServerError, and AsyncOpenAI client.

## Lines 17-24
- Initializes logger and defines OpenAIAgentExecutor class docstring.

## Lines 25-32
- Begins __init__ signature with card/tools/api_key/prompt/base_url.

## Lines 33-40
- Stores card/tools, builds AsyncOpenAI client, sets model/prompt.

## Lines 41-48
- Starts _process_request signature with message/context/updater.

## Lines 49-56
- Builds system/user messages and starts converting tools list.

## Lines 57-64
- Extracts tool schemas and initializes iteration controls.

## Lines 65-72
- Enters loop and issues chat completion request.

## Lines 73-80
- Configures model/messages/tools/tool_choice/temperature/max_tokens.

## Lines 81-88
- Gets assistant message and appends it to conversation history.

## Lines 89-96
- Handles tool_calls, parses function arguments.

## Lines 97-104
- Logs tool call and resolves tool method by name.

## Lines 105-112
- Executes method or returns error if missing.

## Lines 113-120
- Serializes tool result with model_dump/dict/string fallback.

## Lines 121-128
- Appends tool result to messages for follow-up completion.

## Lines 129-136
- Updates task status to working and indicates tool processing.

## Lines 137-144
- Continues loop or, if no tool calls, handles final response.

## Lines 145-152
- Adds final response artifact and completes task.

## Lines 153-160
- Logs OpenAI call error and builds error artifact.

## Lines 161-168
- Adds error artifact, completes task, and exits loop.

## Lines 169-176
- Handles max-iteration fallback and completes task.

## Lines 177-184
- Starts _extract_function_schema with inspect, signature, docstring.

## Lines 185-192
- Extracts description line and initializes schema properties.

## Lines 193-200
- Iterates parameters, sets default types/descriptions.

## Lines 201-208
- Infers types from annotations and tracks required params.

## Lines 209-216
- Builds properties entries and returns schema dict fields.

## Lines 217-224
- Completes schema dict and starts execute signature.

## Lines 225-232
- Creates TaskUpdater, submits task, and starts work.

## Lines 233-240
- Extracts text from message parts into message_text.

## Lines 241-248
- Processes request and logs executor exit.

## Lines 249-252
- cancel raises UnsupportedOperationError via ServerError.
