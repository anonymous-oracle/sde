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
  - Strings: slicing, immutability and the common string methods; formatted output with f-strings and format specifications; `range()`, `break`, loop `else`, `pass`, `del` and `None`
  - Parameters: default, keyword-only and variadic (`*args`, `**kwargs`); scope by the LEGB rule with `global` and `nonlocal`; nested functions and closures
  - Comprehensions (list, dict, set) and generator expressions; `lambda`; higher-order functions (`map`, `filter`, `sorted(key=)`); functions passed as arguments and returned; iterators and generators; `itertools`
  - Functional style: pure functions, immutability, `functools` (`reduce`, `partial`, `lru_cache`); contrast with C's manual memory management (`malloc`/`free`)
  - Standard input and output; text and binary files with `open` and `with`; `pathlib`
- **Environment and tooling**
  - Virtual environments; package management with pip; lock files for reproducibility
  - A hand-built test runner that discovers `test_` functions, then pytest (fixtures, parametrisation, assert rewriting)
  - Editor setup and extensions: VS Code with its language extensions; a debugger run configuration per project; formatter and linter run on save and in CI
  - Print-debugging: printing the state at a suspected fault point, labelled and removed afterwards; what a print shows that stepping and breakpoints do not, and when it is the faster tool
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
  - SciPy: `scipy.optimize` for minimization and root finding; `scipy.stats` distributions and hypothesis tests; `scipy.signal` filters and spectra; each result checked against a hand-built version
  - Seaborn: distribution, categorical and regression plots drawn on Matplotlib axes; figure-level versus axes-level functions; long-form data frames; bootstrapped confidence intervals
  - Plotly: interactive figures rendered in the browser with hover, zoom and linked selections; a dashboard served from Python callbacks
  - FastAPI: async endpoints, Pydantic request and response models, dependency injection, streaming responses, served by Uvicorn

### R for data science

- **The language**: variables and vectors; data frames; `apply`-family functions; user-defined functions and control structures
- **Data handling**: subsetting, merging and joining data frames; matrix operations; the `tidyverse` idiom (`dplyr`, `tidyr`) against base R
- **Graphics**: base plots, histograms, box plots and scatter plots; `ggplot2` basics

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
