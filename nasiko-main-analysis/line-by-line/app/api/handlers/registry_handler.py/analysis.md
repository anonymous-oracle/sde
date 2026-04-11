# registry_handler.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports for FastAPI, AuthClient, and BaseHandler.

## Lines 9-16
- Begins registry-related type imports (create/single/response models).

## Lines 17-24
- Completes type imports and closes the import tuple.

## Lines 25-32
- Defines RegistryHandler, __init__ stores service/logger and sets _search_handler.

## Lines 33-40
- Lazy search_handler property imports SearchHandler and caches instance.

## Lines 41-48
- _index_agent_in_search starts and builds agent_data with id/name/description.

## Lines 49-56
- Adds tags/icon/owner/version/url/created_at/updated_at to agent_data.

## Lines 57-64
- Indexes agent in search, logs debug, warns on failure, starts remove helper.

## Lines 65-72
- _remove_agent_from_search deletes index entry and logs warning on error.

## Lines 73-80
- _transform_registry_to_item_response signature and capabilities_dict setup.

## Lines 81-88
- Normalizes capabilities and begins skills_list comprehension.

## Lines 89-96
- Finishes skills_list and initializes provider_dict handling.

## Lines 97-104
- Converts provider to dict and initializes timestamp strings.

## Lines 105-112
- Formats created_at and begins updated_at formatting.

## Lines 113-120
- Formats updated_at and starts RegistryItemDetailResponse construction.

## Lines 121-128
- Sets id/name/version/description/url and preferredTransport default.

## Lines 129-136
- Sets protocolVersion, provider, and iconUrl with fallback.

## Lines 137-144
- Adds documentationUrl and completes icon/documentation fields.

## Lines 145-152
- Adds capabilities, securitySchemes/security, skills, and starts tags list.

## Lines 153-160
- Finishes tags and sets defaultInputModes/defaultOutputModes.

## Lines 161-168
- Closes defaultOutputModes and starts supportsAuthenticatedExtendedCard.

## Lines 169-176
- Completes supportsAuthenticatedExtendedCard, signatures, and additionalInterfaces.

## Lines 177-184
- Sets created_at/updated_at, closes response, and starts create_registry signature.

## Lines 185-192
- Logs creation, calls service, transforms data, and indexes in search.

## Lines 193-200
- Logs success/returns response and raises 500 on creation failure.

## Lines 201-208
- Handles validation/other errors and starts get_all_registries.

## Lines 209-216
- Logs registry fetch, calls service, initializes list, and starts loop.

## Lines 217-224
- Normalizes capabilities_dict and starts skills_list building.

## Lines 225-232
- Completes skills_list and begins RegistryItemResponse creation.

## Lines 233-240
- Populates item id/db_id/name/version/description/url and preferredTransport start.

## Lines 241-248
- Sets preferredTransport default, capabilities/skills, and begins defaultInputModes.

## Lines 249-256
- Completes defaultInputModes/defaultOutputModes and closes item.

## Lines 257-264
- Appends item, logs count, and begins RegistryResponse.

## Lines 265-272
- Returns RegistryResponse, handles errors, and starts get_registry_by_name.

## Lines 273-280
- Fetches registry by name, transforms, and returns success response.

## Lines 281-288
- Raises 404 when missing and handles HTTPException/other errors.

## Lines 289-296
- get_registry_by_agent_id signature, logging, and service call.

## Lines 297-304
- Transforms/returns on success and raises 404 when missing.

## Lines 305-312
- Handles exceptions and starts get_user_agents signature.

## Lines 313-320
- get_user_agents docstring, reads auth header, raises 401 if missing.

## Lines 321-328
- Uses AuthClient to fetch accessible agent IDs.

## Lines 329-336
- Logs accessible agents returned from auth service.

## Lines 337-344
- Initializes lists, loops over agent IDs with dedupe guard.

## Lines 345-352
- Loads registry and begins description extraction.

## Lines 353-360
- Handles description fallbacks and extracts agent URL.

## Lines 361-368
- Builds capabilities_dict from registry.capabilities.

## Lines 369-376
- Builds skills_list from registry.skills.

## Lines 377-384
- Converts provider to dict when present.

## Lines 385-392
- Begins UserAgentItemResponse with id/name/version/description.

## Lines 393-400
- Adds url/protocolVersion/preferredTransport/provider/icon/documentation.

## Lines 401-408
- Adds capabilities/security/default modes and skills.

## Lines 409-416
- Adds supportsAuthenticatedExtendedCard, signatures, and additionalInterfaces.

## Lines 417-424
- Adds created_at/updated_at, appends user_agent, and starts exception handling.

## Lines 425-432
- Logs error and builds fallback UserAgentItemResponse with core fields.

## Lines 433-440
- Fallback fields for protocol/transport/provider/icon/doc/capabilities/securitySchemes.

## Lines 441-448
- Completes fallback response and appends to list.

## Lines 449-456
- Marks processed, sorts by name, and starts UserAgentsResponse.

## Lines 457-464
- Returns UserAgentsResponse, handles errors, and starts get_my_agents.

## Lines 465-472
- get_my_agents signature/docstring, logs, and reads auth header.

## Lines 473-480
- Raises 401 when missing auth and fetches accessible agent IDs.

## Lines 481-488
- Logs accessible agents for user.

## Lines 489-496
- Initializes lists and starts loop with dedupe.

## Lines 497-504
- Loads registry and begins description extraction.

## Lines 505-512
- Handles description fallbacks and starts icon_url section.

## Lines 513-520
- Resolves icon_url and initializes tags.

## Lines 521-528
- Captures tags and begins SimpleUserAgentResponse with id/name.

## Lines 529-536
- Adds icon_url/tags/description, appends, and starts exception handling.

## Lines 537-544
- Logs debug and builds minimal SimpleUserAgentResponse.

## Lines 545-552
- Appends fallback agent and sorts list.

## Lines 553-560
- Begins error handling and starts minimal agent response construction.

## Lines 561-568
- Completes fallback response and sorts the list.

## Lines 569-576
- Returns SimpleUserAgentsResponse and begins exception handling.

## Lines 577-584
- Handles errors and starts upsert_registry_by_name signature/logging.

## Lines 585-592
- Calls upsert service, transforms data, and indexes in search.

## Lines 593-600
- Logs success/returns response and raises 500 on failure.

## Lines 601-608
- Handles validation/other errors and starts delete_agent_completely.

## Lines 609-616
- delete_agent_completely docstring/logging, calls service, success branch starts.

## Lines 617-624
- Removes from search, logs success, and begins return dict.

## Lines 625-632
- Completes success dict and raises 500 on failure.

## Lines 633-640
- Handles exceptions for deletion and raises 500 on unexpected errors.

## Lines 641-648
- Starts update_agent_version_status signature/docstring and logging.

## Lines 649-656
- Calls update service and begins success response.

## Lines 657-664
- Completes success response and raises 404 when agent missing.

## Lines 665-672
- Handles not-found case and starts generic error handling.

## Lines 673-680
- Logs error and raises 500 for update failures.

## Lines 681-682
- Completes 500 response and ends file.
