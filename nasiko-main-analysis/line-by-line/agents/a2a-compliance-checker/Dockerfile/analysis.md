# Dockerfile — line-by-line analysis

## Lines 1-8
- Uses Python 3.11 slim, sets workdir, copies src, and starts pip install list.

## Lines 9-16
- Installs SDK/CLI/OpenAI/Pydantic/Uvicorn plus MongoDB and LangChain deps.

## Lines 17-24
- Adds document tooling, sets unbuffered output, and runs __main__.py with Mongo args.
