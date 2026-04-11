# __main__.py — line-by-line analysis

## Lines 1-8
- Imports logging/os, click/uvicorn, and A2A server app/request handler modules.

## Lines 9-16
- Imports task store, agent types, dotenv, and OpenAI agent creator.

## Lines 17-24
- Imports executor/Starlette/CORS middleware, loads env vars, and configures logging.

## Lines 25-32
- Declares click command, host/port/mongo options, and starts main.

## Lines 33-40
- Resolves API key, defaults model/base URL, and handles Minimax override.

## Lines 41-48
- Raises missing-key error and starts compliance AgentSkill definition.

## Lines 49-56
- Completes AgentSkill tags/examples for compliance queries.

## Lines 57-64
- Builds AgentCard metadata with name, URL, modes, capabilities, and skills.

## Lines 65-72
- Creates agent data using mongo/db and starts executor configuration.

## Lines 73-80
- Configures OpenAIAgentExecutor with tools, prompt, model, and base URL.

## Lines 81-88
- Builds request handler, A2A app, routes, and Starlette app.

## Lines 89-96
- Adds CORS middleware with allowed origins and headers.

## Lines 97-104
- Finishes CORS config and runs uvicorn server.

## Lines 105-112
- Ends main and starts __main__ guard.

## Lines 113-114
- Invokes main() when executed directly.
