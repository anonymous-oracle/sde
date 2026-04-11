# Dockerfile — line-by-line analysis

## Lines 1-8
- Uses Python 3.11 slim base, sets workdir, copies src, starts pip install list.

## Lines 9-16
- Installs A2A SDK, CLI deps, OpenAI, Pydantic, web stack, GitHub libs, requests.

## Lines 17-20
- Sets unbuffered output and runs agent via __main__.py on port 5000.
