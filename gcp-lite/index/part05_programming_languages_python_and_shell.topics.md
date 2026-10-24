# Part 05 · Programming Languages & Language Theory (part 1 of 3) · TOPIC LIST

Rules and directives for this part: `index/part05_programming_languages_python_and_shell.rules.md`. This file is the topic list only; the Learning method and this domain's prerequisites, depth bar and capstone are in the rules file.

Domain: Programming Languages & Language Theory (part 1 of 3)

### Python

- **Core language**
  - Variables, expressions and control flow
  - Functions, arguments and return values; recursion
  - Built-in data structures: list, dict, set, tuple; the dict as a hash table
  - Classes and object-oriented basics
  - Modules, packages and imports
  - Exceptions, `try`/`finally`, context managers; reading a traceback
- **Environment and tooling**
  - Virtual environments; package management with pip; lock files for reproducibility
  - A hand-built test runner that discovers `test_` functions, then pytest (fixtures, parametrisation, assert rewriting)
- **Python runtime model**
  - Call by sharing; names as references to heap objects; reference counting plus a cycle collector
  - The global interpreter lock and the free-threaded build; `asyncio` as cooperative concurrency
  - Arbitrary-precision `int`; floor division and modulo with negative operands
  - `str` as code points versus `bytes`; `decimal.Decimal` for money
  - Late-binding closures and the mutable-default-argument trap
- **Python for data and services**
  - NumPy: n-dimensional arrays, dtypes and shapes; indexing, slicing and boolean masks; broadcasting; vectorized operations instead of loops; linear-algebra and random routines
  - pandas: DataFrames, selection, grouping, joins, missing values
  - Matplotlib: line, scatter and histogram plots; Jupyter notebooks
  - FastAPI: async endpoints, Pydantic request and response models, dependency injection, streaming responses, served by Uvicorn

### Shell and working with APIs from code

- **Bash scripting**
  - Variables, quoting, loops and conditionals
  - Pipes, redirection and exit codes; `set -euo pipefail`
  - Scripts as glue for CI/CD and automation
  - `jq` for filtering and reshaping JSON on the command line
- **Calling APIs from code**
  - HTTP clients and JSON parsing
  - Cloud SDKs (google-cloud-*, boto3, the Azure SDK)
  - RPC and REST calls from Python and from curl
  - DB-API parameter binding; `psql` against a local Postgres in Docker; file encodings when loading data
