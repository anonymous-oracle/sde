Agents Analysis
===============

Agent Archives
--------------
a2a-compliance-checker.zip
- Type: Zip archive
- Purpose: Packaged copy of `agents/a2a-compliance-checker/`.
- Notes: Not expanded; contents mirror the directory.

a2a-github-agent.zip
- Type: Zip archive
- Purpose: Packaged copy of `agents/a2a-github-agent/`.
- Notes: Not expanded; contents mirror the directory.

a2a-translator.zip
- Type: Zip archive
- Purpose: Packaged copy of `agents/a2a-translator/`.
- Notes: Not expanded; contents mirror the directory.

Compliance Checker Agent
------------------------
Dockerfile
- Type: Container build file
- Purpose: Build a2a-compliance-checker image.

AgentCard.json
- Type: Agent descriptor
- Purpose: Capability metadata, skills, and routing hints.

pyproject.toml
- Type: Packaging config
- Purpose: Dependencies for A2A SDK + OpenAI + Mongo.

README.md
- Type: Documentation
- Purpose: Usage and agent behavior overview.

.gitignore
- Type: VCS ignore rules.

docker-compose.yml
- Type: Local run config.

src/__init__.py
- Type: Package marker.

src/__main__.py
- Type: Entry point
- Purpose: Build AgentCard + executor and run A2A Starlette app.

src/openai_agent_executor.py
- Type: Agent executor
- Purpose: OpenAI tool-calling loop; maps tools to JSON schema; updates task state.

src/openai_agent.py
- Type: Agent factory
- Purpose: Build OpenAI client and tools for executor.

src/compliance_toolset.py
- Type: Toolset
- Purpose: `check_compliance` and `analyze_policy` tooling for LLM.

src/policy_agent.py
- Type: Policy analysis helper
- Purpose: Build policy-specific prompts and responses.
- Notes: Imports `BaseAgent` which is not present in tree (check dependency).

src/agent.py
- Type: Alternate agent flow
- Purpose: LangChain AgentExecutor-based compliance logic (alternate path).

src/tools.py
- Type: Utilities
- Purpose: Web text extraction and helper functions for compliance.

src/models.py
- Type: Pydantic models
- Purpose: JSON-RPC / task schemas used by the agent.

GitHub Agent
------------
Dockerfile
- Type: Container build file.

AgentCard.json
- Type: Agent descriptor.

pyproject.toml
- Type: Packaging config.

README.md
- Type: Documentation.

run_with_phoenix.sh
- Type: Shell script
- Purpose: Run agent with Phoenix tracing enabled.

.gitignore
- Type: VCS ignore rules.

docker-compose.yml
- Type: Local run config.

src/__init__.py
- Type: Package marker.

src/__main__.py
- Type: Entry point
- Purpose: Build AgentCard + executor and run A2A app.

src/openai_agent_executor.py
- Type: Agent executor
- Purpose: OpenAI tool loop with function schema generation.

src/openai_agent.py
- Type: Agent factory
- Purpose: Build OpenAI client and toolset bindings.

src/github_toolset.py
- Type: Toolset
- Purpose: GitHub API operations using PyGithub.

Translator Agent
----------------
Dockerfile
- Type: Container build file.

AgentCard.json
- Type: Agent descriptor.

pyproject.toml
- Type: Packaging config.

README.md
- Type: Documentation.

run_with_phoenix.sh
- Type: Shell script
- Purpose: Run agent with Phoenix tracing enabled.

.gitignore
- Type: VCS ignore rules.

docker-compose.yml
- Type: Local run config.

src/__init__.py
- Type: Package marker.

src/__main__.py
- Type: Entry point
- Purpose: Build AgentCard + executor and run A2A app.

src/openai_agent_executor.py
- Type: Agent executor
- Purpose: OpenAI tool loop with async tool results handling.

src/openai_agent.py
- Type: Agent factory
- Purpose: Build OpenAI client and toolset bindings.

src/translator_toolset.py
- Type: Toolset
- Purpose: Translation, URL extraction, language detection.
