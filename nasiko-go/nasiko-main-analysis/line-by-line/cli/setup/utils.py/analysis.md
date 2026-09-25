# utils.py — line-by-line analysis

## Lines 1-8
- Imports OS/platform utilities, subprocess helpers, and tar/urllib tooling.

## Lines 9-16
- Begins get_tools_dir with docstring describing ~/.nasiko/bin location.

## Lines 17-24
- Documents platform paths and creates tools directory.

## Lines 25-32
- Returns tools dir and starts ensure_helm docstring.

## Lines 33-40
- Resolves helm path, checks global helm, exits early if present.

## Lines 41-48
- Uses cached download if present and prints download start message.

## Lines 49-56
- Detects OS/arch and maps ARM vs AMD64.

## Lines 57-64
- Builds Helm download URL and tar path, prints download info.

## Lines 65-72
- Downloads tarball and extracts helm binary to tools dir.

## Lines 73-80
- Cleans tarball, chmods binary, and adds tools dir to PATH.

## Lines 81-88
- Prints install success and defines _add_to_path helper.

## Lines 89-96
- Starts ensure_terraform docstring and checks global install.

## Lines 97-104
- Resolves tools dir/exe path and returns if already downloaded.

## Lines 105-112
- Adds PATH, prints download message, and detects OS/arch.

## Lines 113-120
- Maps architecture and aborts on unsupported CPU types.

## Lines 121-128
- Builds Terraform download URL and prepares zip path.

## Lines 129-136
- Downloads zip and imports zipfile for extraction.

## Lines 137-144
- Extracts zip, cleans up, and chmods on Unix.

## Lines 145-152
- Adds PATH, prints success, or exits on failure.

## Lines 153-160
- Starts ensure_doctl docstring and checks global install.

## Lines 161-168
- Resolves tools dir path and handles cached download.

## Lines 169-176
- Prints download message and detects OS/arch for doctl.

## Lines 177-184
- Sets arch/version, computes filename and download URL.

## Lines 185-192
- Prepares archive path and downloads from GitHub releases.

## Lines 193-200
- Extracts archive (zip/tar) and deletes archive.

## Lines 201-208
- Chmods binary, adds PATH, prints success, handles errors.

## Lines 209-216
- Exits on doctl install failure and starts ensure_kubectl.

## Lines 217-224
- Checks global kubectl, sets tools dir and binary path.

## Lines 225-232
- Uses cached download or prints download message.

## Lines 233-240
- Detects OS/arch and maps kubectl architectures.

## Lines 241-248
- Handles unsupported arch and fetches stable version URL.

## Lines 249-256
- Reads version, builds download URL, handles Windows suffix.

## Lines 257-264
- Downloads binary, chmods, adds PATH, prints success.

## Lines 265-272
- Handles download errors and exits; starts ensure_aws_cli.

## Lines 273-280
- AWS CLI docstring and global check.

## Lines 281-288
- Sets tools dir path and returns if already installed locally.

## Lines 289-296
- Detects OS/arch and handles Windows case.

## Lines 297-304
- Prints Windows install guidance and exits.

## Lines 305-312
- Prints macOS install guidance and exits.

## Lines 313-320
- Prints Linux download notice and chooses URL by arch.

## Lines 321-328
- Prepares zip path and downloads AWS CLI bundle.

## Lines 329-336
- Extracts zip and locates install script path.

## Lines 337-344
- Runs installer, cleans up zip and temp folder.

## Lines 345-352
- Adds PATH, prints success, handles install errors.

## Lines 353-360
- Starts setup_terraform_modules docstring and purpose.

## Lines 361-368
- Describes args/returns/raises and resolves destination directory.

## Lines 369-376
- Skips extraction if present, handles custom source override.

## Lines 377-384
- Validates custom source path and falls back to bundled extraction.

## Lines 385-392
- Starts _extract_bundled_modules and defines providers mapping.

## Lines 393-400
- Iterates providers, creates dest dirs, and loads package resources.

## Lines 401-408
- Copies .tf files from resources and enters fallback path.

## Lines 409-416
- Falls back to package directory .tf copies if resources fail.

## Lines 417-424
- Raises FileNotFoundError with guidance on extraction failure.

## Lines 425-432
- Verifies aws/digitalocean modules and raises if missing.

## Lines 433-440
- Prints ready message, returns dest, and starts _copy_terraform_from_source.

## Lines 441-448
- Initializes provider list and begins copying from source dirs.

## Lines 449-456
- Checks provider source, warns if missing, and creates provider dirs.

## Lines 457-464
- Lists .tf files, warns if none, and prepares to copy.

## Lines 465-472
- Copies .tf files with force checks and logs copy counts.

## Lines 473-480
- Returns dest and starts get_service_external_ip definition.

## Lines 481-488
- Loads kubeconfig, builds CoreV1Api, and handles errors.

## Lines 489-496
- Prints wait message, sleeps briefly, and starts timer.

## Lines 497-504
- Polls service status and checks load balancer ingress.

## Lines 505-512
- Reads ingress list and begins address extraction.

## Lines 513-520
- Extracts address from ingress object attributes.

## Lines 521-528
- Extracts address from dict, returns when found, handles errors.

## Lines 529-535
- Sleeps between retries and returns pending when timeout reached.
