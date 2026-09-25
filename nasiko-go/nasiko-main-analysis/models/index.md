Models Analysis
===============

ollama/docker-compose.yml
-------------------------
- Type: Docker Compose
- Purpose: Run Ollama LLM server as an optional local model provider.
- Key logic: Mounts model files and start script; exposes port 11434; uses external `agents-net`.
- Inputs/Outputs: HTTP API on port 11434.

ollama/ollama_start.sh
----------------------
- Type: Shell script
- Purpose: Start Ollama server and create a custom model on boot.
- Key logic: `ollama serve` in background, wait for port, `ollama create` with Modelfile.
- Notes: Assumes model file exists under `/root/.ollama/model`.

ollama/model/Modelfile
----------------------
- Type: Ollama Modelfile
- Purpose: Defines a model named `arch-function` from a GGUF file.
- Key logic: `FROM ./arch-function-f16.gguf`, sets `num_ctx 8096`.
