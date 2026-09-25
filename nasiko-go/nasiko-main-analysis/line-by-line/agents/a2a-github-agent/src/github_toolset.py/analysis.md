# github_toolset.py — line-by-line analysis

## Lines 1-8
- Imports os/datetime/typing, GitHub SDK, and Pydantic BaseModel.

## Lines 9-16
- Defines GitHubUser model with optional name/email.

## Lines 17-24
- Defines GitHubRepository model fields and optional metadata.

## Lines 25-32
- Adds repository fields for timestamps/language/stars/forks.

## Lines 33-40
- Defines GitHubCommit model fields.

## Lines 41-48
- Defines base GitHubResponse model fields.

## Lines 49-56
- Defines RepositoryResponse model with repository list.

## Lines 57-64
- Defines CommitResponse model and starts GitHubToolset class.

## Lines 65-72
- Initializes client cache and starts _get_github_client.

## Lines 73-80
- Reads token, configures authenticated or unauthenticated client.

## Lines 81-88
- Returns cached client and starts get_user_repositories signature.

## Lines 89-96
- Documents args/returns and sets default days/limit.

## Lines 97-104
- Fetches user (by name or auth) and handles missing token case.

## Lines 105-112
- Initializes repos list, cutoff date, and iterates updated repos.

## Lines 113-120
- Stops at limit and filters by updated_at cutoff.

## Lines 121-128
- Builds GitHubRepository objects with fields.

## Lines 129-136
- Continues repository fields and optional pushed_at/lang/stars/forks.

## Lines 137-144
- Returns RepositoryResponse success with count and message.

## Lines 145-152
- Handles exceptions and returns error RepositoryResponse.

## Lines 153-160
- Starts get_recent_commits signature and docstring.

## Lines 161-168
- Documents args/returns and sets default days/limit.

## Lines 169-176
- Gets repo, sets cutoff, and begins commits iteration.

## Lines 177-184
- Stops at limit and builds GitHubCommit objects.

## Lines 185-192
- Uses short sha, first-line message, author/date/url fields.

## Lines 193-200
- Returns CommitResponse success with count and message.

## Lines 201-208
- Handles exceptions and returns error CommitResponse.

## Lines 209-216
- Starts search_repositories signature and docstring.

## Lines 217-224
- Documents args/returns and sets default sort/limit.

## Lines 225-232
- Builds recent activity search query and executes search.

## Lines 233-240
- Iterates search results and builds GitHubRepository entries.

## Lines 241-248
- Populates repository fields and optional pushed_at/lang/stars/forks.

## Lines 249-256
- Returns RepositoryResponse success with count/message.

## Lines 257-264
- Handles exceptions and returns error RepositoryResponse.

## Lines 265-272
- Starts get_tools helper and returns tool mapping.

## Lines 273-281
- Returns mapping of tool names to self instance and ends file.
