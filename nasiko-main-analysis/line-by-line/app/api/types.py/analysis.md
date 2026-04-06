# types.py — line-by-line analysis (part 1)

## Lines 1-8
- Imports typing helpers, Pydantic BaseModel, and RegistryBase.
- Declares RegistryCreateRequest and RegistryUpsertRequest as RegistryBase pass-throughs.

## Lines 9-16
- Starts RegistryItemResponse fields (id, db_id, name, version).
- Describes AgentCard id and database _id.

## Lines 17-24
- Adds description, url, preferredTransport and capabilities/skills.
- Defines default input/output modes lists.

## Lines 25-32
- Defines RegistryResponse with data list, status_code, message.

## Lines 33-40
- Starts RegistryItemDetailResponse with agent metadata fields.
- Includes protocolVersion and provider/icon/doc URLs.

## Lines 41-48
- Adds capabilities, securitySchemes, security list.
- Adds default input/output modes and skills list.

## Lines 49-56
- Adds tags, supportsAuthenticatedExtendedCard, signatures.
- Adds additionalInterfaces and timestamps.

## Lines 57-64
- Defines RegistrySingleResponse with detail, status_code, message.

## Lines 65-72
- Defines generic SuccessResponse and TraceData schema start.

## Lines 73-80
- TraceData fields: trace/span identifiers, kind, parent, times.

## Lines 81-88
- TraceData fields: attributes, status, events, links, duration.
- Defines TokenUsage schema start.

## Lines 89-96
- TokenUsage fields input/output/cached/total tokens.
- Starts TraceNode schema with children list.

## Lines 97-104
- TraceNode cost and token cost breakdown fields.

## Lines 105-112
- Defines TracesMetadata (pagination).
- Defines GetTracesResponse schema.

## Lines 113-120
- Defines GetTracesRequest with agent_name and pagination defaults.

## Lines 121-128
- Defines AgentUploadItemResponse schema fields.
- Includes status flags and optional validation_errors/version.

## Lines 129-136
- Defines AgentUploadResponse wrapper with status_code/message.

## Lines 137-144
- Defines AgentDirectoryUploadRequest with directory_path/agent_name.

## Lines 145-152
- Starts UserRegistrationRequest fields.
- Defines UserRegistrationResponse fields (ids, role, status).

## Lines 153-160
- Continues UserRegistrationResponse with access keys and message.

## Lines 161-168
- Starts GitHub API types: GithubUser fields.

## Lines 169-176
- Defines Token schema and GithubLoginResponse.

## Lines 177-184
- Starts GithubRepository schema fields.
- Adds metadata fields like description, privacy, clone URLs.

## Lines 185-192
- Continues repository fields (html_url, default_branch, updated_at).
- Defines GithubRepositoryListResponse with list and total.

## Lines 193-200
- File continues with more API response types beyond line 200.
