# agent_utils.py — line-by-line analysis

## Lines 1-8
- Imports logging/typing, sets logger, and starts truncate_agent_cards with docstring.

## Lines 9-16
- Docstring details args/returns and initializes output list.

## Lines 17-24
- Iterates agent cards, reads name/description, warns and skips when missing.

## Lines 25-32
- Initializes skills list and validates skills type.

## Lines 33-40
- Iterates skills; warns and skips non-dict entries.

## Lines 41-48
- Copies skill dict and removes input/output mode fields.

## Lines 49-56
- Appends cleaned skill and adds truncated card to results.

## Lines 57-63
- Logs processing errors and returns truncated_agent_cards list.
