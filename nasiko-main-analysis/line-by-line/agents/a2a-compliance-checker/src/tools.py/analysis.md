# tools.py — line-by-line analysis

## Lines 1-8
- Docstring and imports for requests, BeautifulSoup, and langchain tool decorator.

## Lines 9-16
- Defines extract_web_text tool signature and docstring arguments.

## Lines 17-24
- Performs HTTP GET, checks status, and parses HTML.

## Lines 25-32
- Removes script/style tags and extracts text content.

## Lines 33-40
- Normalizes whitespace, joins chunks, and truncates output length.

## Lines 41-44
- Returns error message on exceptions.
