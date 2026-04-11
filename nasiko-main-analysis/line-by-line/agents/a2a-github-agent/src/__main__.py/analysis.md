# __main__.py — line-by-line analysis

## Lines 1-8
- Imports logging/os, click/uvicorn, and A2A server app/request handler modules.

## Lines 9-16
- Imports task store, agent types, dotenv, and OpenAI agent creator.

## Lines 17-24
- Imports executor/Starlette, tracing utils, and boots tracing for the agent.

## Lines 25-32
- Loads env vars, configures logging, and defines click command options.

## Lines 33-40
- Starts main, resolves API keys, sets defaults, and handles Minimax override.

## Lines 41-48
- Raises missing-key error and begins AgentSkill definition.

## Lines 49-56
- Defines GitHub skill description, tags, and example prompts.

## Lines 57-64
- Closes skill and starts AgentCard metadata definition.

## Lines 65-72
- Finishes AgentCard and initializes create_agent data.

## Lines 73-80
- Configures OpenAIAgentExecutor with tools, prompt, model, and base URL.

## Lines 81-88
- Builds request handler, A2A app, and routing configuration.

## Lines 89-96
- Creates Starlette app, runs uvicorn, and starts __main__ guard.

## Lines 97-100
- Invokes main() when run as a script.
