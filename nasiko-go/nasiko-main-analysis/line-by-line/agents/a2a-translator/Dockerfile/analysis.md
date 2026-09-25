# Dockerfile — line-by-line analysis

## Lines 1-8
- Uses Python 3.11 slim, sets workdir, copies src, and begins pip install list.

## Lines 9-16
- Installs SDK, CLI, OpenAI, Pydantic, web stack, and requests/BS4/langdetect.

## Lines 17-22
- Adds googletrans, sets unbuffered output, and runs __main__.py on port 5000.
