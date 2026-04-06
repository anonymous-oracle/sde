# cli.py — line-by-line analysis

## Lines 1-8
- Shebang and module docstring for CLI.
- Imports argparse, json, logging, sys, Path.

## Lines 9-16
- Adds current directory to `sys.path` for local imports.
- Imports `AgentCardGeneratorAgent`.

## Lines 17-24
- Sets module logger.
- Defines `main()` and starts argparse parser.

## Lines 25-32
- Adds required agent_path argument and output option.
- Adds verbose flag.

## Lines 33-40
- Adds model option with default `gpt-4o`.
- Adds api-key and n8n-agent flags.

## Lines 41-48
- Parses args and configures logging.

## Lines 49-56
- Sets log level based on verbose; basicConfig format.

## Lines 57-64
- Validates agent_path exists and is directory; exits on error.

## Lines 65-72
- Determines output path default to `AgentCard.json`.
- Logs analysis start and output path.

## Lines 73-80
- If n8n_agent flag: validate `n8n_workflow.json` exists.
- Logs error and exits if missing.

## Lines 81-88
- Logs workflow file usage.
- Initializes AgentCardGeneratorAgent with model and flags.

## Lines 89-96
- Calls `generate_agentcard`; checks for success status.
- Extracts agentcard object on success.

## Lines 97-104
- Writes AgentCard JSON to output file with indent.
- Logs iterations and preview info.

## Lines 105-112
- Handles missing agentcard in success response; exits with warning.

## Lines 113-120
- Handles failure status; exits with error.
- Catches ValueError for missing API keys.

## Lines 121-128
- Logs unexpected exceptions and exits.
- Defines `__main__` guard.

## Lines 129-130
- Invokes `main()` when run as a script.
