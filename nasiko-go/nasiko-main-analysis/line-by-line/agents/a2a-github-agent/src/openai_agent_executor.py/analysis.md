# openai_agent_executor.py — line-by-line analysis

## Lines 1-8
- Imports json/logging/Any and A2A execution/context/event types.

## Lines 9-16
- Imports TaskUpdater, A2A types, ServerError, and AsyncOpenAI.

## Lines 17-24
- Initializes logger and defines OpenAIAgentExecutor class.

## Lines 25-32
- Begins __init__ with card/tools/api_key/prompt/base_url args.

## Lines 33-40
- Stores card/tools, builds AsyncOpenAI client, sets model/prompt.

## Lines 41-48
- Starts _process_request signature and parameters.

## Lines 49-56
- Builds system/user messages and starts tool conversion.

## Lines 57-64
- Extracts schemas for tools and initializes iteration loop vars.

## Lines 65-72
- Enters loop and issues OpenAI chat completion request.

## Lines 73-80
- Sets model/messages/tools/tool_choice/temperature/max_tokens.

## Lines 81-88
- Appends assistant response and tool call metadata.

## Lines 89-96
- Handles tool calls and parses function arguments.

## Lines 97-104
- Logs tool call and resolves tool instance/method.

## Lines 105-112
- Executes method or returns error if missing.

## Lines 113-120
- Serializes results using model_dump/dict/string fallback.

## Lines 121-128
- Appends tool outputs to messages and continues iteration.

## Lines 129-136
- Sends working status update while processing tool calls.

## Lines 137-144
- Continues loop or processes final response content.

## Lines 145-152
- Adds final artifact, completes task, and breaks loop.

## Lines 153-160
- Logs OpenAI errors and prepares error artifacts.

## Lines 161-168
- Adds error artifact, completes task, and exits.

## Lines 169-176
- Handles max-iteration failure response.

## Lines 177-184
- Starts _extract_function_schema with signature/docstring parsing.

## Lines 185-192
- Extracts description and initializes properties/required lists.

## Lines 193-200
- Iterates params and assigns default types/descriptions.

## Lines 201-208
- Infers types from annotations and sets required params.

## Lines 209-216
- Builds property schema entries for OpenAI function format.

## Lines 217-224
- Returns function schema and starts execute signature.

## Lines 225-232
- Creates TaskUpdater, submits task, and starts work.

## Lines 233-240
- Extracts text from message parts to message_text.

## Lines 241-248
- Processes request and logs GitHub agent executor exit.

## Lines 249-252
- cancel raises UnsupportedOperationError through ServerError.
