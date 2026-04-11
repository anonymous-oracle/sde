# buildkit_setup.py — line-by-line analysis

## Lines 1-8
- Imports stdlib/json/base64/typer/yaml/os/Path and Kubernetes helpers.

## Lines 9-16
- Imports Rich helpers and loads importlib.resources files with fallback.

## Lines 17-24
- Initializes Typer app/console and begins get_manifests_dir.

## Lines 25-32
- Locates k8s package and builds manifests path components.

## Lines 33-40
- Converts to Path, returns when found, and ignores lookup errors.

## Lines 41-48
- Builds fallback manifests path from script directory.

## Lines 49-56
- Errors if fallback path missing and returns manifests dir.

## Lines 57-64
- Returns directory and defines load_yaml_manifest with file read.

## Lines 65-72
- Parses YAML or logs error and exits; starts apply_manifest.

## Lines 73-80
- Applies manifest, prints success, or handles already-exists errors.

## Lines 81-88
- Handles create failures or unexpected errors and exits.

## Lines 89-96
- Defines create_registry_secret and builds auth string.

## Lines 97-104
- Encodes auth, loads secret template, and reads dockerconfigjson.

## Lines 105-112
- Replaces placeholders, parses JSON, and updates manifest.

## Lines 113-120
- Applies secret and starts update_deployment_for_auth_method.

## Lines 121-128
- Loads deployment manifest and handles IAM role branch.

## Lines 129-136
- Removes docker-config mounts when using IAM role.

## Lines 137-144
- Cleans placeholder volume mounts list for IAM branch.

## Lines 145-152
- Updates volume mounts and removes docker-config volumes.

## Lines 153-160
- Completes IAM cleanup and enters credentials branch.

## Lines 161-168
- Adds docker-config mount when using username/password credentials.

## Lines 169-176
- Finalizes mounts and starts volume replacement.

## Lines 177-184
- Replaces volume placeholder with docker-config secret.

## Lines 185-192
- Completes secret items and continues volumes update.

## Lines 193-200
- Assigns updated volumes and returns deployment manifest.

## Lines 201-208
- Defines update_serviceaccount_for_iam and loads SA manifest.

## Lines 209-216
- Adds IAM role annotation and returns SA manifest.

## Lines 217-224
- Starts deploy command and registry/username options.

## Lines 225-232
- Adds password/iam_role options and begins deploy docstring.

## Lines 233-240
- Cleans registry URL and computes credential flags.

## Lines 241-248
- Validates auth method and prints usage examples on error.

## Lines 249-256
- Prints example commands and exits on invalid input.

## Lines 257-264
- Resolves manifests dir and starts kubeconfig loading.

## Lines 265-272
- Loads kubeconfig, creates ApiClient, and logs connection.

## Lines 273-280
- Handles kubeconfig errors and exits.

## Lines 281-288
- Starts progress spinner and creates namespace.

## Lines 289-296
- Applies namespace and service account manifests.

## Lines 297-304
- Creates registry secret or logs IAM usage and advances task.

## Lines 305-312
- Creates PVC manifest and advances progress.

## Lines 313-320
- Creates service and prepares deployment manifest.

## Lines 321-328
- Applies deployment, prints success, and computes auth method.

## Lines 329-336
- Prints connection info and backend usage instructions.

## Lines 337-342
- Prints image naming guidance and runs app under __main__.
