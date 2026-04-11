# message_utils.py — line-by-line analysis

## Lines 1-8
- Imports logging/typing, sets logger, and defines extract_text_from_message.

## Lines 9-16
- Docstring describes message parts extraction and returns.

## Lines 17-24
- Validates message not empty and raises ValueError on missing message.

## Lines 25-32
- Ensures message is dict, extracts parts list, validates list type.

## Lines 33-40
- Raises when parts empty; initializes text buffer and counter.

## Lines 41-48
- Iterates parts, skips non-dicts, and filters text parts.

## Lines 49-56
- Concatenates text parts with newlines and logs per-part errors.

## Lines 57-63
- Returns text if found; raises RuntimeError when no text parts present.
