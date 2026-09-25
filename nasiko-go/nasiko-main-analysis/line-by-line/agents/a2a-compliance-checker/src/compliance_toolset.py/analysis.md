# compliance_toolset.py — line-by-line analysis

## Lines 1-8
- Imports logging/typing/BaseModel/PolicyAgent and initializes module logger.

## Lines 9-16
- Defines ComplianceCheckResponse model with status, response, and error fields.

## Lines 17-24
- Starts ComplianceToolset class and __init__ sets agent/session id.

## Lines 25-32
- Defines check_compliance signature and begins docstring for arguments.

## Lines 33-40
- Finishes docstring and sets default compliance query when missing.

## Lines 41-48
- Try block sets document text and logs document length.

## Lines 49-56
- Calls policy agent, returns success response, and starts exception block.

## Lines 57-64
- Logs error, returns error response, and starts analyze_policy definition.

## Lines 65-72
- analyze_policy docstring covers arguments and return model.

## Lines 73-80
- Try block logs question and calls policy agent for response.

## Lines 81-88
- Returns success response or enters error handling.

## Lines 89-96
- Returns error response and defines get_tools helper.

## Lines 97-98
- Returns tool mapping for check_compliance and analyze_policy.
