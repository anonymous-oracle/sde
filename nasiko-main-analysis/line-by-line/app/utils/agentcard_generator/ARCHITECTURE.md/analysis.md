# ARCHITECTURE.md — line-by-line analysis

## Lines 1-8
- Document title and overview section.
- States this agent generates A2A AgentCards and introduces workflow comparison.

## Lines 9-16
- Introduces “What This Agent Does” and begins a numbered workflow list.
- Describes LLM intent and file discovery via `glob_files` and `read_file`.

## Lines 17-24
- Continues workflow list: function analysis and mapping to A2A skills.
- Ends list and starts component breakdown section.

## Lines 25-32
- Introduces tools component (`tools.py`) and its purpose.
- Begins listing tool method signatures in a code block.

## Lines 33-40
- Explains `glob_files` and `read_file` tools.
- Introduces `grep_code` tool signature.

## Lines 41-48
- Describes `grep_code`, `analyze_python_functions`, and metadata extraction.
- Shows `extract_agent_metadata` entry point.

## Lines 49-56
- Notes metadata extraction outputs and `generate_agentcard_json`.
- Ends the tool list code block.

## Lines 57-64
- Introduces agent orchestrator (`agent.py`) and its purpose.
- Starts key components section.

## Lines 65-72
- Shows class skeleton for `AgentCardGeneratorAgent` with init and system prompt.
- Notes LLM initialization and tool loading.

## Lines 73-80
- Lists tool schema and execution methods.
- Shows `generate_agentcard` as the main loop entry.

## Lines 81-88
- Summarizes iterative LLM/tool loop in comments.
- Closes the orchestrator code block.

## Lines 89-96
- Introduces iteration loop example.
- Shows LLM call with tool schemas in pseudocode.

## Lines 97-104
- Demonstrates checking for tool calls and executing them.
- Shows capturing tool call results.

## Lines 105-112
- Adds tool results back to message history.
- Notes continue loop for further LLM processing.

## Lines 113-120
- Ends loop when no tool calls remain.
- Introduces CLI component section.

## Lines 121-128
- Describes CLI purpose and flow.
- Shows user input → validate → run → save output.

## Lines 129-136
- Introduces system prompt section.
- Shows initial system prompt text for AgentCard generation.

## Lines 137-144
- Lists instructions for exploring code and extracting metadata.
- Starts listing available tools.

## Lines 145-152
- Enumerates tools and begins workflow steps.
- Step 1: find files with glob.

## Lines 153-160
- Steps 2–5: read README, analyze functions, map skills, generate JSON.
- Advises focusing on important files.

## Lines 161-168
- Introduces adaptive strategy example.
- Starts scenario 1 (standard structure).

## Lines 169-176
- Iteration 1 and 2: find Python files and read README.
- Prepares for toolset analysis.

## Lines 177-184
- Iteration 3 and 4: analyze toolset and extract metadata.
- Iteration 5: generate AgentCard.

## Lines 185-192
- Ends scenario 1 and starts scenario 2 (missing README).
- Begins second scenario code block.

## Lines 193-200
- Iteration 1 and 2 for missing README: read fails, search docs.
- Shows switching to docs/api.md.

## Lines 201-208
- Iteration 3 reads alternate doc; indicates continuation.
- Introduces function calling flow diagram section.

## Lines 209-216
- Starts ASCII diagram with user request and message initialization.
- Shows system and user roles in the message list.

## Lines 217-224
- Diagram shows LLM analyzing tools and requesting `glob_files`.
- Shows transition arrows between steps.

## Lines 225-232
- Diagram continues: agent executes tool and returns file list.
- Shows handoff back to LLM.

## Lines 233-240
- Diagram shows appending tool result to messages.
- Illustrates tool role entry.

## Lines 241-248
- Diagram shows LLM reading results and requesting README.
- Continues flow arrows.

## Lines 249-256
- Diagram indicates loop continues and reaches final step.
- Shows LLM generating AgentCard request.

## Lines 257-264
- Diagram shows agent executes final tool to create AgentCard.
- Continues to completion.

## Lines 265-272
- Diagram shows LLM final message without tool calls.
- Signals completion state.

## Lines 273-279
- Diagram ends with agent returning result.
