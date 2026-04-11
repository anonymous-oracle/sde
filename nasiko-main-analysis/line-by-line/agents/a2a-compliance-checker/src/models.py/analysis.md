# models.py — line-by-line analysis

## Lines 1-8
- Docstring and imports for uuid, typing, and Pydantic BaseModel/Field.

## Lines 9-16
- Defines MessagePart and begins Message model with role/parts.

## Lines 17-24
- Adds optional messageId and defines JsonRpcParams fields.

## Lines 25-32
- Defines JsonRpcRequest with jsonrpc/id/method/params.

## Lines 33-40
- Defines ArtifactPart and Artifact with uuid default id.

## Lines 41-48
- Defines TaskStatus model with state/timestamp.

## Lines 49-56
- Defines Task model with status/artifacts/contextId.

## Lines 57-60
- Defines JsonRpcResponse wrapper with result Task.
