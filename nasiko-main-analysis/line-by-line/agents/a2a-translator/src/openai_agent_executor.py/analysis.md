# openai_agent_executor.py — line-by-line analysis

## Lines 1-8
- Imports json/logging/inspect/Any and A2A execution/context/event types.

## Lines 9-16
- Imports TaskUpdater, A2A types, ServerError, and AsyncOpenAI client.

## Lines 17-24
- Initializes logger and defines OpenAIAgentExecutor class.

## Lines 25-32
- Begins __init__ with card/tools/api_key/prompt/base_url arguments.

## Lines 33-40
- Stores card/tools, builds AsyncOpenAI client, sets model/prompt.

## Lines 41-48
- Starts _process_request signature and parameters.

## Lines 49-56
- Builds system/user messages and starts tool conversion.

## Lines 57-64
- Builds OpenAI tool schema list and sets iteration counters.

## Lines 65-72
- Enters loop and issues chat completion request.

## Lines 73-80
- Configures model/messages/tools/tool_choice/temperature/max_tokens.

## Lines 81-88
- Appends assistant message and tool call metadata.

## Lines 89-96
- Handles tool calls and parses function arguments.

## Lines 97-104
- Logs tool call and resolves tool instance/method.

## Lines 105-112
- Executes method, awaits coroutine results if needed, or errors.

## Lines 113-120
- Serializes tool results using model_dump/dict/string fallback.

## Lines 121-128
- Appends tool outputs to messages for next iteration.

## Lines 129-136
- Updates task status to working while processing tool calls.

## Lines 137-144
- Continues loop or processes final response content.

## Lines 145-152
- Adds final artifact, completes task, and breaks loop.

## Lines 153-160
- Logs OpenAI errors and builds error artifacts.

## Lines 161-168
- Adds error artifact, completes task, and exits.

## Lines 169-176
- Handles max-iteration error response.

## Lines 177-184
- Starts _extract_function_schema with signature/docstring parsing.

## Lines 185-192
- Extracts description and initializes properties/required lists.

## Lines 193-200
- Iterates params and assigns default type/description.

## Lines 201-208
- Infers types from annotations and sets required params.

## Lines 209-216
- Builds schema properties entries for OpenAI function definition.

## Lines 217-224
- Returns schema dict and starts execute signature.

## Lines 225-232
- Creates TaskUpdater, submits task, and starts work.

## Lines 233-240
- Extracts text from message parts into message_text.

## Lines 241-248
- Processes request and logs translator executor exit.

## Lines 249-256
- cancel raises UnsupportedOperationError via ServerError.

