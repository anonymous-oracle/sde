# entity.py — line-by-line analysis

## Lines 1-8
- Imports datetime, Enum, typing, ObjectId, Pydantic base and core schema.

## Lines 9-16
- Declares PyObjectId class for Pydantic v2 integration.
- Defines core schema hook for serialization.

## Lines 17-24
- Implements validation: accept ObjectId or valid string.
- Raises ValueError for invalid IDs; JSON schema passthrough.

## Lines 25-32
- Completes PyObjectId JSON schema method.
- Starts `Skill` model with id/name/description/tags/examples.

## Lines 33-40
- `Skill` examples allow Any types.
- Defines `Provider` model with organization and optional url.

## Lines 41-48
- Defines `Capabilities` model and default booleans.
- Begins `RegistryBase` model.

## Lines 49-56
- `RegistryBase` fields: protocolVersion, id, name, description, url.
- Preferred transport and provider fields.

## Lines 57-64
- Additional agent metadata: iconUrl, version, documentationUrl.
- Capabilities, securitySchemes, security, defaultInputModes.

## Lines 65-72
- defaultOutputModes, skills, supportsAuthenticatedExtendedCard.
- signatures, additionalInterfaces, tags.

## Lines 73-80
- Owner id and timestamps with defaults.

## Lines 81-88
- `RegistryInDB` adds Mongo `_id` and model_config encoders.

## Lines 89-96
- `UploadStatus` enum values for upload lifecycle.

## Lines 97-104
- `BuildStatus` enum values.
- `AgentBuildBase` fields for build metadata.

## Lines 105-112
- `AgentBuildBase` status, job name, logs fields.

## Lines 113-120
- Build timestamps; `AgentBuildInDB` with `_id` alias.

## Lines 121-128
- `DeploymentStatus` enum values.
- `AgentDeploymentBase` begins with id/agent_id/build_id.

## Lines 129-136
- Deployment fields: namespace, replicas, status, service_url.

## Lines 137-144
- Deployment created_at; `CreateSessionRequest` begins.

## Lines 145-152
- CreateSessionRequest fields for agent_id/agent_url.
- `SessionData` begins.

## Lines 153-160
- SessionData fields for session_id, created_at, title, agent_id.

## Lines 161-168
- SessionData agent_url; `SessionResponse` fields.

## Lines 169-176
- `MessageResponse` fields and metadata.

## Lines 177-184
- `PaginationMetaData` fields for pagination cursors/counts.

## Lines 185-192
- `SessionHistory` fields for session listings.
- `SessionHistoryResponse` begins.

## Lines 193-200
- SessionHistoryResponse fields and defaults.
- `ChatHistory` model begins.

## Lines 201-208
- ChatHistory fields; `ChatHistoryResponse` begins.

## Lines 209-215
- ChatHistoryResponse fields and defaults.
