# container_registry_setup.py — line-by-line analysis

## Lines 1-8
- Imports stdlib/tooling helpers and registry setup utilities.

## Lines 9-16
- Initializes Typer app/console and starts token sanitizer.

## Lines 17-24
- Trims empty tokens and strips accidental quotes.

## Lines 25-32
- _is_do_auth_error detects 401/unauthorized outputs.

## Lines 33-40
- _die_do_auth_hint prints DO auth guidance.

## Lines 41-48
- Prints validation tip and exits; starts _doctl_cmd.

## Lines 49-56
- _doctl_cmd docstring, sanitizes token, returns base command.

## Lines 57-64
- Returns tokenized doctl command; defines _get_digitalocean_token.

## Lines 65-72
- Reads DO token from env aliases and starts normalize helper.

## Lines 73-80
- normalize helper docstring and token lookup.

## Lines 81-88
- Syncs env token vars and returns token.

## Lines 89-96
- run_cmd helper executes subprocess and handles errors.

## Lines 97-104
- Handles missing command errors and starts setup_aws_ecr.

## Lines 105-112
- setup_aws_ecr docstring and prints region config message.

## Lines 113-120
- Fetches AWS account ID and builds registry URL.

## Lines 121-128
- Attempts describe-repositories to detect repo.

## Lines 129-136
- Completes describe command and logs if repo exists.

## Lines 137-144
- Catches describe failure and proceeds to creation attempt.

## Lines 145-152
- Runs create-repository command (idempotent-ish).

## Lines 153-160
- Completes create command and begins login password retrieval.

## Lines 161-168
- Fetches login password, warns about expiry, returns URL/user/pass.

## Lines 169-176
- Starts deploy_ecr_refresher with namespaces and docstring.

## Lines 177-184
- Ensures kubectl and prints deployment message.

## Lines 185-192
- Chooses AWS CLI image and documents refresh logic.

## Lines 193-200
- Builds refresher shell script to fetch token and install kubectl.

## Lines 201-208
- Script loops namespaces and recreates regcred secrets.

## Lines 209-216
- Ends script and begins RBAC manifest string.

## Lines 217-224
- Defines ServiceAccount and ClusterRole in RBAC manifest.

## Lines 225-232
- Adds ClusterRole rules and starts ClusterRoleBinding.

## Lines 233-240
- Completes role binding and begins CronJob manifest.

## Lines 241-248
- Indents script and starts cronjob YAML string.

## Lines 249-256
- Defines CronJob metadata and schedule.

## Lines 257-264
- Sets history limits, job template, service account, container.

## Lines 265-272
- Adds container image/command and restart policy.

## Lines 273-280
- Applies RBAC manifest via kubectl in try block.

## Lines 281-288
- Applies CronJob manifest via kubectl.

## Lines 289-296
- Triggers initial job run with kubectl create job.

## Lines 297-304
- Completes create job args and suppresses output.

## Lines 305-312
- Prints success or handles deploy errors.

## Lines 313-320
- Starts setup_do_registry, normalizes token, errors if missing.

## Lines 321-328
- Prints missing token error, prepares doctl token, runs account get.

## Lines 329-336
- Parses account JSON and extracts email if available.

## Lines 337-344
- Prints authenticated user or warns on parse issues.

## Lines 345-352
- Handles account check failure, captures stderr/stdout.

## Lines 353-360
- Detects auth error and tries context-based doctl auth.

## Lines 361-368
- Warns about stale token, switches to context, or dies on auth.

## Lines 369-376
- Logs inability to verify account details if still failing.

## Lines 377-384
- Prints registry config header and begins existence check.

## Lines 385-392
- Calls doctl registry get and captures output.

## Lines 393-400
- Repeats registry get check and validates auth errors.

## Lines 401-408
- Handles auth errors and proceeds if output available.

## Lines 409-416
- Parses registry info, extracts actual registry name.

## Lines 417-424
- Uses existing registry if name matches; warns otherwise.

## Lines 425-432
- Explains DO single-registry limit and exits on mismatch.

## Lines 433-440
- Handles parse errors and prepares to create registry.

## Lines 441-448
- Prints creation intent and notes default region/tier.

## Lines 449-456
- Builds doctl registry create command with subscription tier.

## Lines 457-464
- Executes create command and handles success/failure.

## Lines 465-472
- Prints created message or handles auth errors.

## Lines 473-480
- Handles duplicate registry errors or existing registry reuse.

## Lines 481-488
- Handles subscription plan error and reports existing registry.

## Lines 489-496
- Prints plan guidance and exits or prints generic failure.

## Lines 497-504
- Logs failure details, uniqueness hints, and exits.

## Lines 505-512
- Builds registry URL and begins credential fetch.

## Lines 513-520
- Runs doctl docker-config, parses JSON, extracts auth entry.

## Lines 521-528
- Validates auth entry and decodes base64 credentials.

## Lines 529-536
- Handles parsing failures and prepares fallback logic.

## Lines 537-544
- Handles invalid token fallback messaging.

## Lines 545-552
- Sets fallback username/password from token and returns.

## Lines 553-560
- Starts deploy command options for provider/region/name.

## Lines 561-568
- Deploy docstring describing AWS vs DO behavior.

## Lines 569-576
- AWS branch: ensure CLI, require region, run setup_aws_ecr.

## Lines 577-584
- DO branch: ensure doctl, run setup_do_registry, else error.

## Lines 585-592
- Prints configured registry and returns credentials.

## Lines 593-600
- deploy command options close and docstring describes behavior.

## Lines 601-608
- Docstring continues and AWS branch validates region.

## Lines 609-616
- Runs AWS setup, handles DO setup, and branches for errors.

## Lines 617-624
- Handles unsupported provider, prints success, returns creds.

## Lines 625-626
- __main__ guard runs the Typer app.
