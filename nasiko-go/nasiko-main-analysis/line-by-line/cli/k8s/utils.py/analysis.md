# utils.py — line-by-line analysis

## Lines 1-8
- Module docstring, imports OS/tempfile/yaml/pathlib/Console setup.

## Lines 9-16
- Defines create_dynamic_helm_values and begins docstring.

## Lines 17-24
- Documents args/returns/errors and initializes values_file.

## Lines 25-32
- Writes temp YAML file, logs success, and returns path.

## Lines 33-40
- Handles exceptions by logging, deleting temp file, and re-raising.

## Lines 41-48
- Starts deploy_helm_chart signature and documents arguments.

## Lines 49-56
- Continues docstring and validates helm_runner requirement.

## Lines 57-64
- Notes ensure_helm, creates dynamic values file, and begins helm_cmd.

## Lines 65-72
- Builds helm upgrade/install command arguments.

## Lines 73-80
- Adds namespace and values file flags, then checks env values file.

## Lines 81-88
- Adds environment values file and logs its usage.

## Lines 89-96
- Appends additional args and runs helm_runner.

## Lines 97-104
- Cleans up temporary values file in finally block.

## Lines 105-112
- Defines cleanup_helm_values_file and deletes temp file.

## Lines 113-120
- Logs cleanup failure and starts validate_helm_values docstring.

## Lines 121-128
- Documents args/returns/errors and short-circuits if no required keys.

## Lines 129-136
- Iterates key paths, walking nested dict for each requirement.

## Lines 137-144
- Collects missing keys and raises ValueError if any missing.

## Lines 145-150
- Returns True when validation passes.
