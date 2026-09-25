# k8s_setup.py — line-by-line analysis

## Lines 1-8
- Docstring describing k8s CLI purpose and state/module paths.

## Lines 9-16
- Docstring notes backend support and begins imports.

## Lines 17-24
- Imports helpers, console, and terraform state utilities.

## Lines 25-32
- Imports terraform_state helpers and defines default cluster name.

## Lines 33-40
- Creates Typer app and console instance.

## Lines 41-48
- Provider enum defines aws/digitalocean values.

## Lines 49-56
- _run_command signature and docstring for subprocess runs.

## Lines 57-64
- Describes args and prepares environment/important keywords.

## Lines 65-72
- Builds environment and keyword list for output filtering.

## Lines 73-80
- Continues keywords list for Terraform output filtering.

## Lines 81-88
- Starts Popen streaming and prints important lines or dots.

## Lines 89-96
- Configures Popen with cwd/env/pipe settings.

## Lines 97-104
- Prints output lines or dots while process runs.

## Lines 105-112
- Waits for process and raises on nonzero exit.

## Lines 113-120
- Handles missing command and command failure errors.

## Lines 121-128
- Raises Typer exit and begins get_tf_output docstring.

## Lines 129-136
- get_tf_output args/returns and prepares env vars.

## Lines 137-144
- Runs `terraform output -raw` and returns value.

## Lines 145-152
- Returns None on error and starts _prepare_tf_vars.

## Lines 153-160
- Normalizes node_size OptionInfo and starts TF var mapping.

## Lines 161-168
- Sets TF_VAR_cluster_name and AWS region/instance type.

## Lines 169-176
- Sets DO region/node size and loads token envs.

## Lines 177-184
- Prompts for DO token if missing and stores in env.

## Lines 185-192
- Returns tf_vars and begins create command decorator.

## Lines 193-200
- create command args for provider/name/region.

## Lines 201-208
- Adds node_size/auto_approve/verbose options.

## Lines 209-216
- Adds terraform_dir/state_dir options.

## Lines 217-224
- create docstring describing state backend defaults.

## Lines 225-232
- Ensures tools and prints cluster creation start info.

## Lines 233-240
- Sets up working directory and handles missing modules.

## Lines 241-248
- Prints state info and prepares Terraform env vars.

## Lines 249-256
- Runs terraform init with prepared environment.

## Lines 257-264
- Runs terraform plan and prepares apply command.

## Lines 265-272
- Runs terraform apply and starts addon verification.

## Lines 273-280
- AWS addon verification via terraform outputs and aws cli.

## Lines 281-288
- Warns if addon missing or prints verification success.

## Lines 289-296
- Handles verify errors and starts kubeconfig setup.

## Lines 297-304
- Determines kubeconfig path and begins provider-specific setup.

## Lines 305-312
- Runs aws eks update-kubeconfig and chmods file.

## Lines 313-320
- Writes DO kubeconfig, sets env, prints success.

## Lines 321-328
- Handles kubeconfig errors and starts storage class patch.

## Lines 329-336
- Patches gp2 storageclass default and handles errors.

## Lines 337-344
- Warns on patch failure and starts destroy command.

## Lines 345-352
- destroy command args for provider/name/auto_approve/verbose.

## Lines 353-360
- Adds terraform_dir/state_dir/cleanup options.

## Lines 361-368
- destroy docstring, ensures tools, prints start message.

## Lines 369-376
- Checks state existence and exits if missing.

## Lines 377-384
- Gets work_dir, prints state info, prepares env vars.

## Lines 385-392
- Runs terraform init and destroy with auto-approve.

## Lines 393-400
- Prints completion and optionally cleans state.

## Lines 401-408
- Starts output command options for provider/name/dirs.

## Lines 409-416
- output docstring, ensures terraform, prints status.

## Lines 417-424
- Validates state existence and builds env vars.

## Lines 425-432
- Runs terraform output and starts list command.

## Lines 433-440
- list command state_dir option and docstring.

## Lines 441-448
- Lists clusters or prints none-found guidance.

## Lines 449-456
- Prints managed clusters heading and loops clusters.

## Lines 457-464
- Computes state file status and prints cluster info.

## Lines 465-472
- Ends list output and starts state_info command.

## Lines 473-480
- state_info args and docstring, loads state info.

## Lines 481-488
- Prints backend type and module/state flags.

## Lines 489-496
- Prints state file path and calls print_state_info.

## Lines 497-504
- Starts init-modules command options.

## Lines 505-512
- init-modules docstring and usage description.

## Lines 513-520
- Prints example, runs setup_terraform_modules.

## Lines 521-528
- Checks module existence and prints status.

## Lines 529-536
- Warns on missing modules and suggests command.

## Lines 537-544
- Validates state existence for outputs and prepares env vars.

## Lines 545-552
- Runs terraform output and begins list_clusters command.

## Lines 553-560
- list_clusters option for state_dir and docstring.

## Lines 561-568
- Loads clusters and prints guidance when none exist.

## Lines 569-576
- Prints managed clusters header and iterates entries.

## Lines 577-584
- Determines state status and prints cluster/state info.

## Lines 585-592
- Prints spacing and starts state_info command definition.

## Lines 593-600
- state_info options for provider/cluster/state_dir.

## Lines 601-608
- state_info docstring, loads state info, prints header.

## Lines 609-616
- Prints backend type and module/state flags.

## Lines 617-624
- Prints state file path and calls print_state_info.

## Lines 625-632
- init-modules options and docstring header.

## Lines 633-640
- init-modules docstring detailing purpose and behavior.

## Lines 641-648
- Prints example, runs setup_terraform_modules.

## Lines 649-656
- Checks aws/do module files and prints status header.

## Lines 657-664
- Prints module status, location, and warns if missing.

## Lines 665-672
- Prints missing module guidance and runs app in __main__.
