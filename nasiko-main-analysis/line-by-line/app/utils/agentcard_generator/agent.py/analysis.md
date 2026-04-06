# agent.py — line-by-line analysis (part 1)

## Lines 1-8
- Module docstring describes the AgentCard generator agent.
- Imports JSON/logging/os/sys/Path/typing and OpenAI client.

## Lines 9-16
- Adds current directory to `sys.path` for local imports.
- Imports `AgentAnalyzerTools` and initializes logger.

## Lines 17-24
- Declares `AgentCardGeneratorAgent` class and docstring.

## Lines 25-32
- Starts `__init__` signature with api_key, model, n8n_agent, base_url.

## Lines 33-40
- `__init__` docstring defines args and purpose.
- Notes API key can be OpenAI or MiniMax.

## Lines 41-48
- Reads API key from args or env vars; validates presence.
- Logs error and raises ValueError if missing.

## Lines 49-56
- Detects MiniMax usage when OpenAI key absent.
- Sets base_url and default MiniMax model.

## Lines 57-64
- Logs init, instantiates OpenAI client, stores model/tools.
- Sets max_iterations and n8n_agent flag.

## Lines 65-72
- Logs debug for initialization.
- Begins `_get_system_prompt`.

## Lines 73-80
- For n8n_agent, returns long system prompt for workflow-based cards.
- Describes goal and available tools for n8n mode.

## Lines 81-88
- Outlines critical workflow for reading workflow JSON.
- Emphasizes parsing name, chat trigger, and agent node.

## Lines 89-96
- Lists capability derivation rules (streaming, push, state history).
- Defaults unspecified capabilities to false.

## Lines 97-104
- Describes skill derivation from workflow prompt and system message.
- Specifies skill fields: id, name, description, tags, examples, modes.

## Lines 105-112
- Notes input/output modes for n8n chat workflows.
- Introduces description generation requirements.

## Lines 113-120
- Guides AgentCard generation with transport/mode defaults.
- Emphasizes explicit capability mapping only.

## Lines 121-128
- Lists conservative rules for n8n capabilities.
- Returns to general (non-n8n) system prompt text.

## Lines 129-136
- General prompt: analyze agent code and A2A capabilities.
- Lists tools: glob, read, grep, analyze functions, metadata.

## Lines 137-144
- Adds transport detection tool and AgentCard generation.
- Begins critical workflow steps.

## Lines 145-152
- Step 1: find key files with glob patterns.
- Step 2: read A2A server implementation.

## Lines 153-160
- Explains reading __main__/executor files for setup and capabilities.
- Starts framework detection guidance.

## Lines 161-168
- Instructs use of `detect_agent_framework`, candidate evaluation rules.

## Lines 169-176
- Prioritizes orchestration frameworks and ignores protocol libs.
- Begins transport detection guidance.

## Lines 177-184
- Details `detect_transport_protocol` usage and evidence sources.
- Notes pass-through to generate_agentcard_json.

## Lines 185-192
- Begins A2A capability detection criteria (streaming).
- Lists indicators for SSE/streaming support.

## Lines 193-200
- Continues pushNotifications criteria (webhooks/notifications).

## Lines 201-208
- Lists stateTransitionHistory detection cues and rule (any TaskStore).

## Lines 209-216
- Defines chat_agent detection criteria for non-A2A chat APIs.
- Notes OpenAI-style chat endpoints and direct chat routes.

## Lines 217-224
- Finalizes chat_agent rule; begins input/output mode analysis guidance.

## Lines 225-232
- Describes default input/output modes and image output handling.
- Starts function/tool extraction guidance.

## Lines 233-240
- Emphasizes analyzing real tool implementations over existing AgentCards.
- Defines skill mapping fields (id, name, description, tags, examples).

## Lines 241-248
- Completes skill mapping guidance and begins AgentCard generation step.

## Lines 249-256
- Lists AgentCard generation inputs and accuracy warnings.
- Ends system prompt string.

## Lines 257-264
- Starts `_get_tool_schemas`; branches for n8n_agent tool schema list.
- Defines glob_files tool schema for n8n mode.

## Lines 265-272
- Defines glob_files parameters and required fields.
- Begins read_file tool schema.

## Lines 273-280
- read_file schema for n8n workflow JSON.
- Starts generate_agentcard_json schema for n8n mode.

## Lines 281-288
- Defines agent_name and description fields in schema.
- Begins skills array schema.

## Lines 289-296
- Defines skill object properties (id, name, description, tags, examples).

## Lines 297-304
- Adds inputModes/outputModes properties and required list.
- Adds preferred_transport field.

## Lines 305-312
- Adds default_input_modes/output_modes definitions for n8n.
- Adds streaming/push/state history fields.

## Lines 313-320
- Marks required fields and ends n8n schema list.
- Begins default (non-n8n) schema list.

## Lines 321-328
- Defines glob_files schema for non-n8n mode.
- Specifies pattern and base_path fields.

## Lines 329-336
- Finalizes glob_files schema and begins read_file schema.

## Lines 337-344
- Defines read_file schema parameters and required list.

## Lines 345-352
- Begins grep_code schema with pattern and file_path fields.

## Lines 353-360
- Adds case_sensitive option and required fields for grep_code.
- Ends grep_code schema.

## Lines 361-368
- Begins analyze_python_functions schema with file_path parameter.

## Lines 369-376
- Ends analyze_python_functions schema; begins extract_agent_metadata schema.

## Lines 377-384
- Defines extract_agent_metadata schema with agent_path parameter.

## Lines 385-392
- Ends extract_agent_metadata schema; begins detect_transport_protocol schema.

## Lines 393-400
- Defines detect_transport_protocol schema parameters and required list.

## Lines 401-408
- Completes detect_transport_protocol schema parameters.
- Begins read_file schema for non-n8n tools (continued).

## Lines 409-416
- Ends read_file schema and starts grep_code schema.
- Sets name and description for grep_code.

## Lines 417-424
- Defines grep_code parameters: pattern and file_path.
- Adds regex description.

## Lines 425-432
- Adds case_sensitive boolean and required list for grep_code.
- Ends grep_code schema.

## Lines 433-440
- Starts analyze_python_functions schema and description.
- Defines file_path parameter.

## Lines 441-448
- Completes analyze_python_functions schema.
- Starts extract_agent_metadata schema.

## Lines 449-456
- Defines extract_agent_metadata parameters and required list.
- Ends extract_agent_metadata schema.

## Lines 457-464
- Starts detect_transport_protocol schema with detailed description.
- Defines file_path parameter.

## Lines 465-472
- Completes detect_transport_protocol schema.
- Starts detect_agent_framework schema.

## Lines 473-480
- Defines detect_agent_framework description and file_path parameter.
- Ends detect_agent_framework schema.

## Lines 481-488
- Starts generate_agentcard_json schema with description.
- Opens parameters object.

## Lines 489-496
- Adds agent_name and description fields.
- Starts skills array schema with object properties.

## Lines 497-504
- Defines skill properties: id, name, description, tags.

## Lines 505-512
- Adds examples and inputModes/outputModes for skills.
- Adds required list for skill object.

## Lines 513-520
- Adds port and version fields for AgentCard generation.

## Lines 521-528
- Adds streaming and push_notifications capability flags.

## Lines 529-536
- Adds state_transition_history and chat_agent flags.
- Adds default_input_modes/output_modes arrays.

## Lines 537-544
- Adds preferred_transport and additional_interfaces fields.
- Specifies additional_interfaces item schema.

## Lines 545-552
- Adds agentFramework field description.
- Declares required fields (agent_name, description, skills).

## Lines 553-560
- Closes generate_agentcard_json schema definition.

## Lines 561-568
- Continues list closure for tools schema array.

## Lines 569-576
- Completes tool schema list (end of return list).

## Lines 577-584
- Ends `_get_tool_schemas` method return list.

## Lines 585-592
- Defines additional_interfaces array schema and item properties.
- Lists url and transport fields for each interface.

## Lines 593-600
- Adds agentFramework field description.
- Prepares required field list and closes schema objects.

## Lines 601-608
- Declares required fields and closes schema list.
- Ends `_get_tool_schemas` and starts `_execute_tool` definition.

## Lines 609-616
- Logs tool execution and checks tool existence.
- Calls tool method and logs result status.

## Lines 617-624
- Returns result on success; logs error and returns error dict when tool missing.
- Starts `generate_agentcard` method signature.

## Lines 625-632
- Docstring for generate_agentcard; describes args and return structure.

## Lines 633-640
- Sets success tool name and handles n8n workflow path.
- Logs and builds user message for n8n case.

## Lines 641-648
- Builds default user message for non-n8n case.
- Initializes messages list with system/user roles.

## Lines 649-656
- Initializes iteration count and final_agentcard.
- Starts loop with max_iterations and logs iteration.

## Lines 657-664
- Prints iteration header when verbose.
- Begins try block and logs LLM call.

## Lines 665-672
- Calls OpenAI chat completions with tools and temperature.
- Sets max_tokens and captures response.

## Lines 673-680
- Extracts message and logs tool call count.
- Builds assistant_message with content.

## Lines 681-688
- Adds tool_calls to assistant_message when present.
- Appends assistant message to messages list.

## Lines 689-696
- Prints assistant content when verbose.
- If tool_calls exist, begins loop over them.

## Lines 697-704
- Extracts tool_name and arguments JSON for each tool call.

## Lines 705-712
- Logs tool call and prints verbose arguments.
- Executes tool via `_execute_tool`.

## Lines 713-720
- Prints success/failure messages when verbose.
- Checks for successful AgentCard generation tool.

## Lines 721-728
- Stores generated AgentCard and logs success.
- Appends tool result message to conversation.

## Lines 729-736
- Adds tool role message with tool_call_id and JSON result.
- Continues loop to next tool call.

## Lines 737-744
- Continues to next iteration after tool calls.
- Logs completion and prints finished banner if verbose.

## Lines 745-752
- Breaks out of loop when no more tool calls.
- Catches exceptions and returns error response.

## Lines 753-760
- Returns error payload with message and null agentcard.
- Handles max-iterations reached with warning and error response.

## Lines 761-768
- Returns success payload with generated AgentCard and iteration count.

## Lines 769-772
- Ends method and class definition.
