# file_utils.py — line-by-line analysis

## Lines 1-8
- Imports base64/logging/typing and defines encode_file_to_filepart signature.

## Lines 9-16
- Docstring describes encoding file to file part structure.

## Lines 17-24
- Opens file, base64 encodes contents, and builds filename.

## Lines 25-32
- Returns file part dict with bytes/name payload.

## Lines 33-40
- Handles FileNotFound and PermissionError with logging/raised errors.

## Lines 41-48
- Handles generic errors and defines make_text_part signature/docstring.

## Lines 49-56
- Returns text part dict for message payloads.

## Lines 57-57
- (No additional code; file ends after make_text_part.)
