# terraform_state.py — line-by-line analysis

## Lines 1-8
- Module docstring explains Terraform state management responsibilities.

## Lines 9-16
- Docstring describes architecture paths and remote backend usage.

## Lines 17-24
- Docstring closes and imports os/shutil/Path/Optional.

## Lines 25-32
- Imports Console and config helpers, initializes console.

## Lines 33-40
- Defines setup_working_directory signature and parameters.

## Lines 41-48
- Docstring explains working directory creation steps.

## Lines 49-56
- Docstring lists arguments and return value details.

## Lines 57-64
- Resolves terraform source and provider module path; checks existence.

## Lines 65-72
- Prints helpful error messages and raises FileNotFoundError.

## Lines 73-80
- Gets working directory and copies modules if missing.

## Lines 81-88
- Generates backend config, logs work dir, and returns it.

## Lines 89-96
- Defines _copy_terraform_modules helper and its purpose.

## Lines 97-104
- Sets file extensions/excludes and iterates source items.

## Lines 105-112
- Copies .tf/.tfvars files and standard config files.

## Lines 113-120
- Completes copy helper and starts backend config function docstring.

## Lines 121-128
- Reads backend config, prepares backend.tf path.

## Lines 129-136
- Deletes existing backend.tf, reads backend type, and starts local content.

## Lines 137-144
- Builds local backend documentation and configuration string.

## Lines 145-152
- Finishes local backend content with terraform local block.

## Lines 153-160
- Handles S3 backend settings and begins S3 content string.

## Lines 161-168
- Adds S3 backend fields and optional DynamoDB lock table.

## Lines 169-176
- Finalizes S3 backend content and starts GCS branch.

## Lines 177-184
- Builds GCS backend content with bucket/prefix.

## Lines 185-192
- Finalizes GCS backend content and starts Terraform Cloud branch.

## Lines 193-200
- Builds Terraform Cloud backend content with org/workspace.

## Lines 201-208
- Completes Terraform Cloud content or uses local fallback.

## Lines 209-216
- Writes backend.tf content to disk.

## Lines 217-224
- Defines get_cluster_state_info signature and docstring.

## Lines 225-232
- Describes returned info and resolves work_dir/backend_config.

## Lines 233-240
- Builds initial info dict with backend type and state fields.

## Lines 241-248
- Detects module presence and local state file existence.

## Lines 249-256
- Marks state existence, sets state_file, and returns info.

## Lines 257-264
- Defines list_managed_clusters signature and docstring.

## Lines 265-272
- Resolves state root path from args/env or nasiko home.

## Lines 273-280
- Initializes cluster list and iterates provider directories.

## Lines 281-288
- Iterates cluster directories and checks for terraform markers.

## Lines 289-296
- Appends cluster info dicts for directories with state/modules.

## Lines 297-304
- Returns clusters list and starts cleanup_cluster_state docstring.

## Lines 305-312
- Describes cleanup intent and resolves work_dir.

## Lines 313-320
- Removes working directory and logs cleanup.

## Lines 321-325
- Removes empty provider directory after cleanup.
