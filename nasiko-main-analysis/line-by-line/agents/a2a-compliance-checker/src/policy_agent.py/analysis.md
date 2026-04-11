# policy_agent.py — line-by-line analysis

## Lines 1-8
- Imports logging/BaseAgent, sets logger, and starts PolicyAgent class.

## Lines 9-16
- Docstring and get_response signature; logs request and starts system prompt.

## Lines 17-24
- Builds system prompt with document under review and policy list intro.

## Lines 25-32
- Lists policy rules 1-7 including tone, PII, IFRS, expenses, encryption.

## Lines 33-40
- Adds work hours/internal comms policies and scope constraints.

## Lines 41-48
- Defines analysis method and conversation abilities.

## Lines 49-56
- Specifies interaction guidance and response format headers.

## Lines 57-64
- Defines response format details and evidence/fix fields.

## Lines 65-72
- Builds user_prompt, calls agent chat, logs snippet, returns response.
