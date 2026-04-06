# __main__.py — line-by-line analysis

## Lines 1-8
- Imports logging, os, click, uvicorn, A2A server classes.
- Imports AgentCard/AgentCapabilities/AgentSkill and dotenv.

## Lines 9-16
- Imports create_agent and WebhookAgentExecutor.
- Imports Starlette; loads dotenv and configures logging.

## Lines 17-24
- Defines click CLI options for host/port.
- Starts main function and checks WEBHOOK_URL.

## Lines 25-32
- Raises error if WEBHOOK_URL missing.
- Defines AgentSkill with id, name, description, tags, examples.

## Lines 33-40
- Builds AgentCard with URL, version, modes, capabilities, skills.

## Lines 41-48
- Calls create_agent factory and builds executor.
- Creates DefaultRequestHandler with InMemoryTaskStore.

## Lines 49-56
- Builds A2AStarletteApplication and routes.
- Creates Starlette app and runs uvicorn.

## Lines 57-64
- __main__ guard invokes main().
