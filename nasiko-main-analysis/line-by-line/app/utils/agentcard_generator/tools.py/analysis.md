# tools.py — line-by-line analysis (part 1)

## Lines 1-8
- Module docstring describes tools for analyzing agent code.
- Imports AST, logging, regex, and Path utilities.

## Lines 9-16
- Imports typing helpers, sets module logger.
- Defines `AgentAnalyzerTools` class and its docstring.

## Lines 17-24
- `glob_files` method signature and docstring start.
- Documents pattern and base_path arguments.

## Lines 25-32
- Describes return structure and logs the glob action.
- Initializes base path and checks existence.

## Lines 33-40
- Handles missing base path with warning and error response dict.

## Lines 41-48
- Builds glob matches list; filters files.
- Logs count and returns success response with files.

## Lines 49-56
- Catches generic exceptions; logs error and returns error response.

## Lines 57-64
- `read_file` method starts with docstring and args.
- Declares return structure and logs read attempt.

## Lines 65-72
- Opens file, reads content, splits into lines.

## Lines 73-80
- Logs line count and returns success dict with content.

## Lines 81-88
- Handles FileNotFoundError with warning and error response.

## Lines 89-96
- Handles other exceptions with error logging and response.

## Lines 97-104
- `grep_code` method signature and docstring start.
- Lists args for pattern, file_path, case sensitivity.

## Lines 105-112
- Describes return value and logs search start.

## Lines 113-120
- Opens file and reads content.
- Sets regex flags and initializes matches; begins line iteration.

## Lines 121-128
- Appends regex matches with line number and stripped content.
- Logs match count and prepares success response dict.

## Lines 129-136
- Returns match metadata (file_path, pattern, matches, count).
- Handles generic exceptions with logging and error response.

## Lines 137-144
- Closes error response for grep.
- Starts `analyze_python_functions` definition and docstring.

## Lines 145-152
- Documents args/returns and logs analysis start.
- Opens file and reads content.

## Lines 153-160
- Parses AST; on SyntaxError returns error with empty functions list.

## Lines 161-168
- Initializes functions list; walks AST for function definitions.

## Lines 169-176
- Skips private/dunder functions.
- Begins parameter extraction, skipping `self`.

## Lines 177-184
- Initializes return_type and inspects annotations.
- Uses `ast.unparse` when available.

## Lines 185-192
- Fallbacks for return type and suppresses parsing errors.
- Extracts docstring and first-line summary.

## Lines 193-200
- Builds function metadata dict (name, description, params, return type, line).

## Lines 201-208
- Appends function metadata to list.
- Logs count and returns success response.

## Lines 209-216
- Returns function list and count with file_path.
- Handles analysis exceptions with error response.

## Lines 217-224
- Error response includes message and empty functions list.
- Starts `extract_agent_metadata` signature and docstring.

## Lines 225-232
- Logs extraction start and builds base_path metadata dict.
- Initializes agent_name, description, dependencies.

## Lines 233-240
- Reads README if present; logs file path.
- Reads file content for description extraction.

## Lines 241-248
- Uses regex to capture first paragraph after title.
- Stores description and logs preview.

## Lines 249-256
- Begins dependency extraction from pyproject.toml.
- Opens and reads file content for dependency parsing.

## Lines 257-264
- Regex extracts dependency list, parses quoted deps.
- Normalizes dependency names by splitting on `>=`.

## Lines 265-272
- Silently ignores parsing errors.
- Logs metadata extraction success and prepares response.

## Lines 273-280
- Returns success status with metadata payload.
- Handles extraction errors with logging.

## Lines 281-288
- Returns error status and empty metadata on failure.
- Starts `detect_transport_protocol` signature and docstring.

## Lines 289-296
- Describes AST-based detection for transport protocols.
- Lists analysis techniques and supported transports.

## Lines 297-304
- Documents args and return dict structure for detection output.

## Lines 305-312
- Logs detection start; opens and reads file content.

## Lines 313-320
- Ends docstring block and logs detection start.
- Opens file and reads content into memory.

## Lines 321-328
- Parses AST; on syntax error returns error with JSONRPC fallback.

## Lines 329-336
- Begins local import detection for app creation helpers.
- Iterates ImportFrom nodes and builds module name.

## Lines 337-344
- Filters out stdlib-ish modules and dots; checks alias names.
- Adds modules with “app” or “create” in imported names.

## Lines 345-352
- Logs possible app creation imports and stores in list.

## Lines 353-360
- Prepares to analyze additional files for local imports.
- Resolves module path and queues for analysis.

## Lines 361-368
- Logs additional files and initializes evidence/transports.
- Builds file list to analyze (main + extra).

## Lines 369-376
- Iterates each file; if extra file, reads and parses AST.
- Skips file if parsing fails.

## Lines 377-384
- Uses main AST for primary file.
- Begins import analysis over the AST.

## Lines 385-392
- For ImportFrom nodes: captures module and imported names.
- Detects a2a.server imports as JSONRPC evidence.

## Lines 393-400
- Detects RPC-related import names and adds JSONRPC transport.
- Starts REST/HTTP indicators for FastAPI and Flask.

## Lines 401-408
- Logs FastAPI usage as evidence (no transport set).
- Adds HTTP+JSON when Flask imported.

## Lines 409-416
- Detects WebSocket imports and records transport/evidence.

## Lines 417-424
- Starts call analysis; flags A2A usage on call names.
- Looks for A2A setup calls.

## Lines 425-432
- Marks A2A detection and records evidence.
- Handles attribute calls for `.routes()` / `.build()`.

## Lines 433-440
- Adds evidence for A2A method calls and JSONRPC transport.
- Notes default A2A transport behavior.

## Lines 441-448
- Begins decorator analysis for REST vs RPC endpoints.
- Normalizes decorator strings with `ast.unparse` if available.

## Lines 449-456
- Looks for REST endpoint decorators (app/router HTTP verbs).
- Excludes generic RPC endpoints by path patterns.

## Lines 457-464
- If REST endpoint detected and not already JSONRPC, adds HTTP+JSON.
- Records evidence for REST endpoint.

## Lines 465-472
- Determines preferred transport from collected transports.
- Assigns confidence level based on transport type.

## Lines 473-480
- Defaults to JSONRPC with low confidence when no evidence.
- Adds fallback evidence note.

## Lines 481-488
- Computes additional_transports list excluding preferred.
- Logs detected transport and begins return payload.

## Lines 489-496
- Returns success payload with preferred transport, confidence, evidence.
- Handles remaining transport cases.

## Lines 497-504
- Completes return payload, additional transports, and status.
- Starts exception handler for detection errors.

## Lines 505-512
- Logs error and returns error status with JSONRPC fallback.

## Lines 513-520
- Completes error return payload.
- Starts `detect_agent_framework` definition and docstring.

## Lines 521-528
- Describes detection strategy: recursive import analysis.
- Emphasizes orchestration frameworks over SDKs; ignores transport libs.

## Lines 529-536
- Documents args/return format for framework detection.
- Logs detection start.

## Lines 537-544
- Initializes traversal state: visited files, queue, import set.
- Computes base directory for module resolution.

## Lines 545-552
- Iterates file queue; skips already visited files.
- Skips missing files.

## Lines 553-560
- Reads and parses file content into AST.
- Logs parse failures and continues.

## Lines 561-568
- Walks AST and collects root modules from `import` statements.

## Lines 569-576
- Handles `from ... import ...` nodes and relative import placeholders.
- Adds root module names for non-relative imports.

## Lines 577-584
- Builds module path to follow local imports.
- Queues local module file for further analysis.

## Lines 585-592
- Checks module_path exists and not visited before enqueue.
- Notes placeholder for imported-name modules.

## Lines 593-600
- Initializes evidence and candidates lists.
- Starts large stdlib module exclusion set.

## Lines 601-608
- Lists common stdlib modules to filter (os, sys, json, logging, asyncio).

## Lines 609-616
- Continues stdlib set (typing, datetime, time, pathlib, re, math, random, uuid, abc).

## Lines 617-624
- Continues stdlib set (argparse, functools, itertools, collections, copy, threading).

## Lines 625-632
- Continues stdlib set (subprocess, warnings, io, tempfile, shutil, glob, gzip).

## Lines 633-640
- Continues stdlib set (tarfile, zipfile, csv, unittest, doctest, pydoc, inspect, traceback).

## Lines 641-648
- Continues stdlib set (pdb, pickle, shelve, dbm, sqlite3, zlib, hashlib, hmac).

## Lines 649-656
- Continues stdlib set (secrets, urllib, http, ftplib, smtplib, poplib, imaplib, nntplib).

## Lines 657-664
- Continues stdlib set (telnetlib, xml, html, cgi, socket, ssl, select, selectors).

## Lines 665-672
- Continues stdlib set (asyncore, asynchat, signal, mmap, email, json, base64, binascii).

## Lines 673-680
- Continues stdlib set (quopri, contextlib, dataclasses, enum, numbers, decimal, fractions, statistics, textwrap).

## Lines 681-688
- Finishes stdlib set (string, struct, codecs, unicodedata).
- Computes non-stdlib imports list.

## Lines 689-696
- Declares orchestration frameworks mapping (CrewAI, LangChain, LlamaIndex, AutoGen, PhiData, Semantic Kernel).

## Lines 697-704
- Iterates framework map; checks exact or prefix matches in imports.
- Adds high-confidence orchestration candidates.

## Lines 705-712
- Adds evidence strings for found orchestration frameworks.

## Lines 713-720
- Starts direct LLM SDK detection section and mapping.
- Includes OpenAI, Anthropic, Google, Mistral, Cohere, MiniMax.

## Lines 721-728
- Iterates SDK map; handles special case for google.generativeai.
- Adds candidate and evidence for google SDK.

## Lines 729-736
- Handles general SDK imports via exact/prefix matching.
- Adds medium-confidence SDK candidates.

## Lines 737-744
- Records evidence for SDK usage.
- Starts protocol library detection section.

## Lines 745-752
- Lists protocol/transport libraries (a2a, fastapi, flask, starlette, uvicorn, etc.).

## Lines 753-760
- Adds evidence entries for protocol libraries (not framework).
- Logs candidates and returns success payload.

## Lines 761-768
- Returns candidates, non-stdlib imports, evidence.
- Starts exception handler for framework detection.

## Lines 769-776
- Logs error and returns error payload with empty lists.
- Begins `generate_agentcard_json` signature and args.

## Lines 777-784
- Lists required parameters and defaults for card generation.
- Continues options for streaming/push/history/chat flags.

## Lines 785-792
- Adds input/output modes, transport, additional interfaces, agentFramework.
- Starts docstring for generation.

## Lines 793-800
- Documents args like skills, port, version, streaming options.

## Lines 801-808
- Documents push notifications, state history, chat agent, input/output modes.

## Lines 809-816
- Documents preferred transport and additional interfaces.
- Notes return dict shape.

## Lines 817-824
- Logs generation start and parameters.
- Sets defaults for input/output modes.

## Lines 825-832
- Defines `normalize_mime` for shorthand conversion.
- Handles `text`, `json`, `image` shorthands.

## Lines 833-840
- Applies normalization to input/output mode lists.
- Starts building AgentCard dict.

## Lines 841-848
- Sets protocolVersion, name, description, URL, framework, transport.
- Fills provider metadata.

## Lines 849-856
- Adds icon URL, version, documentation URL.
- Adds capabilities map.

## Lines 857-864
- Adds security fields and input/output modes.
- Adds skills, authenticated card flag, signatures.

## Lines 865-872
- Conditionally adds additionalInterfaces if provided.
- Logs count of additional interfaces.

## Lines 873-880
- Returns success payload with generated AgentCard.
- Starts exception handler for generation.

## Lines 881-888
- Logs generation errors; returns error payload.

## Lines 889-896
- Defines `get_available_tools` and docstring.
- Returns list of tool method names.

## Lines 897-904
- Continues tool name list through detect/generate methods.

## Lines 905-906
- Closes tools list and method.

## Continuation
- Further line chunks continue in the next update.
