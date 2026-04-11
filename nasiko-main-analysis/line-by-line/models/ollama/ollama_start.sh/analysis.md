# ollama_start.sh — line-by-line analysis

## Lines 1-8
- Starts bash script, launches ollama server, stores PID.

## Lines 9-16
- Polls server port until ready and logs readiness.

## Lines 17-24
- Creates model from Modelfile and waits for server process.
