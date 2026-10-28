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
  - Standard input and output; text and binary files with `open` and `with`; `pathlib`; reading a text file line by line by iterating the file object, so memory stays bounded; the read modes `'r'`, `'rb'`, `'w'` and `'a'` and what each does to an existing file (`'w'` truncates it, `'a'` appends); explicit `encoding='utf-8'` on text files, and the newline translation that text mode performs
- **Environment and tooling**
  - Virtual environments; package management with pip; lock files for reproducibility
  - A hand-built test runner that discovers `test_` functions, then pytest (fixtures, parametrisation, assert rewriting)
  - Editor setup and extensions: VS Code with its language extensions; a debugger run configuration per project; formatter and linter run on save and in CI; text editing as a skill: multi-file search and replace, a language server that supplies diagnostics, go-to-definition and rename, and running in the integrated terminal the same test command that CI runs; for Go, the official Go extension with `gopls` as the language server, with `gofmt` and `go vet` run on save
  - Print-debugging: printing the state at a suspected fault point, labelled and removed afterwards; what a print shows that stepping and breakpoints do not, and when it is the faster tool
  - Notebooks and scripts: a Jupyter notebook is an ordered list of cells whose outputs are saved in the file, so cells run out of order leave hidden state that a fresh run does not reproduce; restart the kernel and run all cells before trusting a result; move reused logic into an importable module, keeping the notebook for exploration, and run that logic as a script from the command line with a checked exit code
- **Python runtime model**
  - Call by sharing; names as references to heap objects; reference counting plus a cycle collector
  - The global interpreter lock and the free-threaded build; `asyncio` as cooperative concurrency
  - Arbitrary-precision `int`; floor division and modulo with negative operands
  - `str` as code points versus `bytes`; `decimal.Decimal` for money
  - Late-binding closures and the mutable-default-argument trap
- **Python for data and services**
  - NumPy: n-dimensional arrays, dtypes and shapes; indexing, slicing and boolean masks; broadcasting; vectorized operations instead of loops; linear-algebra and random routines; strides and views, where a slice shares memory with its base array while .copy() and fancy indexing make a new array; seeded generators with numpy.random.default_rng(seed) for reproducible draws; numpy.linalg.solve for Ax = b, inv, det, eig for eigenvalues and eigenvectors, and norm; axis reasoning, where a reduction over axis k removes that axis from the shape and `keepdims=True` keeps it as length 1; dtype reasoning, where fixed-width integers wrap silently on overflow and mixing integer and float arrays promotes the result to float
  - pandas: DataFrames, selection, grouping, joins, missing values; the index as the row label that aligns data across operations; groupby as split-apply-combine; merge with its inner, left and outer joins and the row count each produces; NaN for missing floats, with the nullable dtypes for missing integers and strings
  - Matplotlib: line, scatter and histogram plots; Jupyter notebooks; subplots and GridSpec layouts, contour and heatmap plots, and savefig to write a figure to a file; 3D surface and scatter plots through `projection='3d'` on the axes, and savefig with `dpi` and `bbox_inches='tight'` so that labels are not clipped
  - SciPy: `scipy.optimize` for minimization and root finding; `scipy.stats` distributions and hypothesis tests; `scipy.signal` filters and spectra; each result checked against a hand-built version; `scipy.signal.butter` designs a Butterworth filter returned as second-order sections, `filtfilt` applies it forward and backward for zero phase, and `welch` estimates a power spectral density by averaging windowed periodograms, whose frequency resolution is the sampling rate divided by the segment length
  - Seaborn: distribution, categorical and regression plots drawn on Matplotlib axes; figure-level versus axes-level functions; long-form data frames; bootstrapped confidence intervals
  - Plotly: interactive figures rendered in the browser with hover, zoom and linked selections; a dashboard served from Python callbacks; dashboards as operations tools, with panels for latency, traffic, errors and saturation, each answering one question, and every alert linked to a runbook that names its trigger, the first checks with their exact commands, the mitigation and the rollback, and who to escalate to
  - FastAPI: async endpoints, Pydantic request and response models, dependency injection, streaming responses, served by Uvicorn
  - LangChain, LlamaIndex, vLLM and Ray, taught as service concepts rather than reimplemented: LangChain composes prompt templates, model calls, output parsers and tool calls into chains; LlamaIndex builds a retrieval pipeline that splits documents into nodes, embeds them, retrieves the top-k by similarity and passes them to a response synthesizer; vLLM serves LLMs with a paged KV cache that allocates attention state in fixed-size blocks and batches requests continuously; Ray runs tasks and actors across a cluster, passing large objects by reference through its object store

### R for data science

- **The language**: variables and vectors; data frames; `apply`-family functions; user-defined functions and control structures
- **Data handling**: subsetting, merging and joining data frames; matrix operations; the `tidyverse` idiom (`dplyr`, `tidyr`) against base R
- **Graphics**: base plots, histograms, box plots and scatter plots; `ggplot2` basics

### Shell and working with APIs from code

- **Bash scripting**
  - Variables, quoting, loops and conditionals
  - Pipes, redirection and exit codes; `set -euo pipefail`
  - Scripts as glue for CI/CD and automation; a Python script with an `if __name__ == "__main__"` entry point, arguments read by argparse, and subprocess.run calls whose exit codes are checked
  - `jq` for filtering and reshaping JSON on the command line
- **Calling APIs from code**
  - HTTP clients and JSON parsing
  - Cloud SDKs (google-cloud-*, boto3, the Azure SDK)
  - RPC and REST calls from Python and from curl
  - DB-API parameter binding; `psql` against a local Postgres in Docker; file encodings when loading data
