# translator_toolset.py — line-by-line analysis

## Lines 1-8
- Imports HTTP/async utilities, parsing, Pydantic, HTML parsing, and language detection.

## Lines 9-16
- Sets deterministic language detection seed and starts TranslationRequest model.

## Lines 17-24
- Adds source/target language fields and begins URLTranslationRequest model.

## Lines 25-32
- Adds URL translation fields and defines LanguageDetectionRequest model.

## Lines 33-40
- Adds text/url fields and begins TranslationResult model fields.

## Lines 41-48
- Completes TranslationResult, starts LanguageDetectionResult model.

## Lines 49-56
- Adds detection result fields and starts TranslationResponse base model.

## Lines 57-64
- Adds status/message fields and defines TextTranslationResponse model.

## Lines 65-72
- Adds text response data and defines URLTranslationResponse fields.

## Lines 73-80
- Adds URL response fields and defines LanguageDetectionResponse.

## Lines 81-88
- Starts TranslatorToolset with session setup and User-Agent header.

## Lines 89-96
- Begins _translate_with_google signature and docstring.

## Lines 97-104
- Builds Google Translate URL and query parameters.

## Lines 105-112
- Sends request, checks status, and parses JSON response.

## Lines 113-120
- Concatenates translated segments from response list.

## Lines 121-128
- Extracts detected source language and returns translation.

## Lines 129-136
- Raises translation error and begins _extract_text_from_url docstring.

## Lines 137-144
- Documents args/returns and validates URL format.

## Lines 145-152
- Fetches URL and parses HTML, removes scripts/styles.

## Lines 153-160
- Extracts page title and body/whole document text.

## Lines 161-168
- Cleans text by stripping lines and chunking phrases.

## Lines 169-176
- Joins cleaned text, returns text/title, and handles errors.

## Lines 177-184
- Starts _detect_language docstring with args/returns.

## Lines 185-192
- Detects language from sample text or returns unknown.

## Lines 193-200
- Starts async translate_text docstring and arguments.

## Lines 201-208
- Validates non-empty text and begins language auto-detect.

## Lines 209-216
- Detects language and defines blocking translate helper.

## Lines 217-224
- Runs translation in executor and returns translated text.

## Lines 225-232
- Handles translation errors and begins translate_url docstring.

## Lines 233-240
- Documents URL translation args/return value.

## Lines 241-248
- Extracts text, handles empty content, and continues.

## Lines 249-256
- Truncates long text and auto-detects source language.

## Lines 257-264
- Translates extracted content and returns result.

## Lines 265-272
- Handles errors and begins detect_language docstring.

## Lines 273-280
- Validates text/url inputs and rejects both provided.

## Lines 281-288
- Errors on missing inputs or extracts text from URL.

## Lines 289-296
- Validates text, detects language, and returns code.

## Lines 297-304
- Handles errors and defines get_tools mapping.

## Lines 305-307
- Returns tool mapping for translate_text/url/detect_language.
