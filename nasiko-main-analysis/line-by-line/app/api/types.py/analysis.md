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

## Lines 201-208
- Defines GithubCloneRequest with repository_full_name, branch, agent_name.
- Starts UploadStatusItemResponse class.

## Lines 209-216
- UploadStatusItemResponse fields: upload_id, agent_name, status, progress.
- Adds owner_id, source_info, file_size, capabilities_generated.

## Lines 217-224
- Adds orchestration/registry flags, url, registry_id, status_message.
- Adds error_details, validation_errors, created_at.

## Lines 225-232
- Adds updated_at, completed_at, processing/orchestration duration.
- Starts UploadStatusResponse with data list.

## Lines 233-240
- UploadStatusResponse status_code/message.
- Defines UploadStatusSingleResponse wrapper.

## Lines 241-248
- UploadStatusSingleResponse fields; UploadStatusListResponse fields.
- Starts UploadStatusUpdateRequest schema.

## Lines 249-256
- Update fields: status/progress/status_message/url/registry_id.
- Flags for capabilities/orchestration/registry updates.

## Lines 257-264
- Adds error/validation lists and duration fields.
- Starts AgentBuildRequest with agent_id.

## Lines 265-272
- AgentBuildRequest adds github_url/version_tag.
- Starts AgentDeployRequest (agent_id, build_id, port).

## Lines 273-280
- Documents default port 5000 and env_vars optional.
- Starts AgentBuildStatusUpdateRequest.

## Lines 281-288
- Build status update fields: agent_id, github_url, version_tag, image_reference.
- Adds status, logs, k8s_job_name, error_message.

## Lines 289-296
- Starts AgentDeploymentStatusUpdateRequest with agent_id/build_id/status.
- Adds service_url and k8s_deployment_name.

## Lines 297-304
- Adds namespace and error_message; starts UserAgentItemResponse.
- Begins core agent info (id).

## Lines 305-312
- Adds name/version/description/url.
- Adds protocolVersion and preferredTransport.

## Lines 313-320
- Adds provider/icon/docs fields.
- Starts capabilities/config fields.

## Lines 321-328
- Adds securitySchemes/security/default modes/skills/support flags/signatures.
- Adds additionalInterfaces.

## Lines 329-336
- Adds upload_id and timestamps.
- Starts UserAgentsResponse fields.

## Lines 337-344
- UserAgentsResponse message.
- Starts UploadInfoResponse with upload_type/status.

## Lines 345-352
- Defines SimpleUserUploadAgentResponse fields.
- Includes upload_info, tags, description.

## Lines 353-360
- Defines SimpleUserAgentResponse fields.
- Includes icon_url, tags, description.

## Lines 361-368
- Defines SimpleUserUploadAgentsResponse wrapper.
- Adds status_code/message.

## Lines 369-376
- Defines SimpleUserAgentsResponse wrapper.
- Starts UserSearchResult schema.

## Lines 377-384
- UserSearchResult fields: id, username, display_name, email, role, avatar_url, score.

## Lines 385-392
- Starts AgentSearchResult with agent_id/agent_name/description/tags/icon_url/owner_id.

## Lines 393-400
- Adds version and score fields for agent search result.
- Starts UserSearchResponse with data list.

## Lines 400-407
- UserSearchResponse adds query, total_matches, showing, status_code, message.
- Starts AgentSearchResponse class.

## Lines 408-415
- AgentSearchResponse fields mirror UserSearchResponse for agents.
- Begins Agent Update API Types section.

## Lines 416-423
- Defines AgentVersionInfo fields: version, status, created_at, build/deploy ids.
- Adds optional git_commit and rollback_info.

## Lines 424-431
- Starts AgentUpdateRequest with version and update strategy.
- Adds cleanup_old flag.

## Lines 432-439
- Adds optional description for update request.
- Starts AgentUpdateResponse with message/agent_id/new_version.

## Lines 440-447
- Adds previous_version/build_id/deployment_id/update_strategy/status/status_code.

## Lines 448-455
- Starts AgentRollbackRequest with target_version/cleanup_failed/reason.
- Starts AgentRollbackResponse with message/agent_id.

## Lines 456-463
- Adds rolled_back_to/rolled_back_from/status/status_code.
- Starts AgentVersionHistoryResponse.

## Lines 464-471
- AgentVersionHistoryResponse fields: agent_id/current_version/versions/status_code/message.
- Starts AgentRebuildRequest.

## Lines 472-479
- AgentRebuildRequest fields reason/force.
- Starts AgentRebuildResponse fields.

## Lines 480-487
- AgentRebuildResponse fields: message/agent_id/version/build_id/status/status_code.
- Starts Version Mapping section and VersionMappingRequest.

## Lines 488-495
- VersionMappingRequest fields: agent_id, semantic_version.
- VersionMappingResponse fields: agent_id, semantic_version, image_tag, timestamp.

## Lines 496-503
- VersionMappingResponse adds status_code/message.
- Starts VersionStatusUpdateRequest with status field.

## Lines 504-511
- VersionStatusUpdateResponse fields: agent_name, status, status_code, message.
- Starts NANDA API Types section.

## Lines 512-519
- Defines NANDAAgentFacts fields (username, ids, agent_name, label, description, version, documentationUrl).

## Lines 520-527
- Adds jurisdiction, provider, endpoints, capabilities, skills, evaluations, telemetry.

## Lines 528-535
- Adds certification, userId, created_at, updated_at, iotMetadata.
- Starts NANDAAgent class.

## Lines 536-543
- NANDAAgent fields: id, name, description, endpoint, status, category, factsUrl, agentFacts.

## Lines 544-551
- Adds lastSeen, messageCount, specialties, subCategory.
- Starts NANDAPagination schema.

## Lines 552-559
- NANDAPagination fields: page, limit, total, totalPages, hasNext, hasPrev.
- Starts NANDAAgentsResponse.

## Lines 560-567
- NANDAAgentsResponse fields: agents, pagination.
- Starts NANDAAgentsListRequest with type/limit/page.

## Lines 568-575
- Adds status/category/search filters.
- Starts NANDAAgentDetailResponse.

## Lines 576-583
- NANDAAgentDetailResponse fields: agent, status_code, message.
- Starts NANDAApiResponse fields.

## Lines 584-591
- NANDAApiResponse fields: success, data, message, status_code.
- Starts NANDA Messages API Types and NANDAMessageContent.

## Lines 592-599
- NANDAMessageContent fields message/raw_response.
- Starts NANDAMessage with _id, timestamp, type, from/to agent, content, conversation_id.

## Lines 600-607
- NANDAMessage adds agent_id, response_to, from_region, to_region.
- Starts NANDAMessagesResponse with messages list.

## Lines 608-615
- NANDAMessagesResponse adds total and has_more.
- Starts NANDAMessagesListRequest with limit/offset/before/after.

## Lines 616-620
- NANDAMessagesListRequest adds agent_id, conversation_id, message_type filters.
- End of file.
