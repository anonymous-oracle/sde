# config.py — line-by-line analysis

## Lines 1-8
- Docstring describing config sources and precedence overview.

## Lines 9-16
- Notes priority order and Terraform state management defaults.

## Lines 17-24
- Imports os/json/Path/typing and initializes Console.

## Lines 25-32
- Defines _ensure_dir_permissions docstring and arguments.

## Lines 33-40
- Sets permissions and walks parent directories with chmod.

## Lines 41-48
- Handles chmod failures and starts constants section.

## Lines 49-56
- Defines default public registry user and starts env var mapping.

## Lines 57-64
- Maps provider/region/cluster/kubeconfig and registry type vars.

## Lines 65-72
- Maps registry credentials, domain/email, and OpenAI key.

## Lines 73-80
- Maps public registry, superuser, GitHub OAuth, and terraform dirs.

## Lines 81-88
- Maps backend config variables and DynamoDB locking.

## Lines 89-96
- Maps Terraform Cloud vars and begins config file search list.

## Lines 97-104
- Lists config file search paths and ends list.

## Lines 105-112
- find_config_file docstring and parameters.

## Lines 113-120
- Handles explicit config path, warning if missing.

## Lines 121-128
- Searches cwd for config files and returns first match.

## Lines 129-136
- Returns None and starts load_config_file docstring.

## Lines 137-144
- Explains env loading behavior and arguments.

## Lines 145-152
- Attempts dotenv import and warns if missing.

## Lines 153-160
- Loads env file without override and logs success.

## Lines 161-168
- Returns True if loaded, else False.

## Lines 169-176
- get_env_var docstring describing args/returns.

## Lines 177-184
- Resolves env var mapping and returns value or default.

## Lines 185-192
- print_config_summary prints header and config file path.

## Lines 193-200
- Defines key vars list for summary output.

## Lines 201-208
- Adds OpenAI/DO/AWS vars and iterates list.

## Lines 209-216
- Masks sensitive values before printing.

## Lines 217-224
- Prints non-sensitive values and trailing blank line.

## Lines 225-232
- validate_required_credentials docstring and args.

## Lines 233-240
- Initializes missing list and checks AWS access key.

## Lines 241-248
- Checks AWS secret and DigitalOcean token variants.

## Lines 249-256
- Records missing DO token and returns list.

## Lines 257-264
- get_nasiko_home creates ~/.nasiko and sets permissions.

## Lines 265-272
- get_default_terraform_dir creates terraform directory.

## Lines 273-280
- Returns tf dir and starts get_terraform_dir docstring.

## Lines 281-288
- Describes terraform dir precedence and args.

## Lines 289-296
- Handles CLI override path and warning on missing.

## Lines 297-304
- Handles NASIKO_TERRAFORM_DIR env var and warnings.

## Lines 305-312
- Falls back to default terraform dir and starts get_state_dir.

## Lines 313-320
- get_state_dir docstring and state path description.

## Lines 321-328
- Lists args/returns and begins state_root resolution.

## Lines 329-336
- Resolves state_root from override/env/default.

## Lines 337-344
- Creates state_dir, fixes permissions, and returns it.

## Lines 345-352
- get_backend_config docstring and backend description.

## Lines 353-360
- Lists backend types and reads backend_type env var.

## Lines 361-368
- Handles local backend and begins s3 config.

## Lines 369-376
- Builds s3 config and optional DynamoDB table.

## Lines 377-384
- Warns on missing bucket and falls back to local.

## Lines 385-392
- Returns s3 config or starts gcs config.

## Lines 393-400
- Builds gcs config and warns on missing bucket.

## Lines 401-408
- Builds remote config and validates organization.

## Lines 409-416
- Warns on missing org and returns remote config.

## Lines 417-424
- Handles unknown backend types with local fallback.

## Lines 425-432
- get_cluster_credentials_file docstring and path rules.

## Lines 433-440
- Continues docstring with args/returns.

## Lines 441-448
- Creates creds dir, fixes permissions, returns file path.

## Lines 449-456
- get_cluster_info_file docstring and args.

## Lines 457-464
- Creates info dir, fixes permissions, returns info path.

## Lines 465-472
- save_cluster_info docstring and resolves info file.

## Lines 473-480
- Merges existing info with new data.

## Lines 481-488
- Writes JSON, chmods file, logs warning on failure.

## Lines 489-496
- get_cluster_api_url docstring and args.

## Lines 497-504
- Initializes state_root for cluster lookup and returns None if missing.

## Lines 505-512
- Iterates provider dirs and finds cluster info file.

## Lines 513-520
- Reads cluster info JSON, returns gateway_url, or continues.

## Lines 521-528
- Returns None and begins list_clusters docstring.

## Lines 529-536
- list_clusters docstring and return description.

## Lines 537-544
- Initializes clusters/state_root and starts provider loop.

## Lines 545-552
- Filters provider/cluster dirs and sets info_file path.

## Lines 553-560
- Builds cluster_info dict and checks info_file existence.

## Lines 561-568
- Loads info_file data, updates cluster_info, and sets url.

## Lines 569-576
- Appends cluster_info, returns clusters, starts print_state_info.

## Lines 577-584
- Prints state config header and local backend info.

## Lines 585-592
- Prints local backup tip and starts s3 backend info.

## Lines 593-600
- Prints s3 details and begins gcs backend info.

## Lines 601-608
- Prints gcs prefix and starts remote backend info.

## Lines 609-611
- Prints remote workspace and trailing blank line.
