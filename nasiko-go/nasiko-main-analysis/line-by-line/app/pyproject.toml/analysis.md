# app/pyproject.toml — line-by-line analysis

## Lines 1-8
- Declares project metadata: name, version, description, Python >=3.12.
- Starts dependency list with web/utility packages (asgiref, bs4, black).

## Lines 9-16
- Adds click, FastAPI, LangChain core/community/openai, langtrace, nltk.

## Lines 17-24
- Adds motor, numexpr, openpyxl, OpenTelemetry distro/exporter/instrumentation.

## Lines 25-32
- Adds OTEL instrumentation (openai), pandas + stubs, pydantic, pypdf2, python-docx, requests.

## Lines 33-40
- Adds pydantic-settings, soupsieve, uvicorn, wikipedia, docx, pymongo, OTLP HTTP exporter.

## Lines 41-48
- Adds Phoenix/OpenInference, astor, toml, anthropic, google-generativeai, crewai, autogen, django, flask.

## Lines 49-56
- Adds httpx, aiohttp, boto3, pinecone, chromadb, redis, psycopg2-binary, sqlalchemy.

## Lines 57-64
- Adds python-multipart, typer, rich, a2a, a2a-server, elasticsearch, pydo, kubernetes.

## Lines 65-72
- Adds pyyaml and semver; closes dependencies list.
- Starts dev dependency group with pyinstaller.

## Lines 73-73
- Closes the dev dependency group list.
