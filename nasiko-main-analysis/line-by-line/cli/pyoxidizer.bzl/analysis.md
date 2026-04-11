# pyoxidizer.bzl — line-by-line analysis

## Lines 1-8
- Header comments describe PyOxidizer config purpose and targets.

## Lines 9-16
- Starts make_exe and describes default Python distribution usage.

## Lines 17-24
- Creates packaging policy and notes allow_files option.

## Lines 25-32
- Documents in-memory shared library loading and bytecode options.

## Lines 33-40
- Notes bytecode optimization settings and extension filter options.

## Lines 41-48
- Describes minimal/no-libraries extension filter behavior.

## Lines 49-56
- Documents no-copyleft filter and file scanner classify option.

## Lines 57-64
- Describes file scanner emit and include_classified_resources toggle.

## Lines 65-72
- Notes include_distribution_sources/resources toggles.

## Lines 73-80
- Notes include_file_resources/non_distribution_sources and include_test.

## Lines 81-88
- Explains resource location and fallback behavior.

## Lines 89-96
- Sets filesystem-relative resource location and variant hint.

## Lines 97-104
- Notes resource handling mode options (classify/files).

## Lines 105-112
- Describes interpreter config and creates python_config.

## Lines 113-120
- Notes config_profile and module_search_paths options.

## Lines 121-128
- Documents allocator backend options (jemalloc/mimalloc).

## Lines 129-136
- Documents snmalloc/default allocator and allocator_raw.

## Lines 137-144
- Documents allocator_mem/allocator_obj and pymalloc arena flags.

## Lines 145-152
- Documents allocator_debug and multiprocessing auto/none options.

## Lines 153-160
- Notes explicit multiprocessing start methods and importer toggles.

## Lines 161-168
- Notes sys.frozen/sys.meipass and module write directory options.

## Lines 169-176
- Notes run_command/run_module/run_filename and sets run_module main.

## Lines 177-184
- Builds PythonExecutable with name, policy, and config.

## Lines 185-192
- Notes tcl/tk support and Windows DLL handling (never/when-present).

## Lines 193-200
- Notes Windows DLL always mode and subsystem selection.

## Lines 201-208
- Documents pip download/install resource options.

## Lines 209-216
- Notes pip_install comment and adds nasiko-cli resources.

## Lines 217-224
- Notes resource filtering and returns exe; starts embedded resources.

## Lines 225-232
- Defines make_embedded_resources and make_install layout.

## Lines 233-240
- Returns install files and starts MSI builder function.

## Lines 241-248
- Defines MSI builder parameters for id/name/version.

## Lines 249-256
- Adds MSI author and opens code signing section.

## Lines 257-264
- register_code_signers checks ENABLE_CODE_SIGNING and returns.

## Lines 265-272
- Comments describe pfx-based code signing prompts.

## Lines 273-280
- Comments describe pfx signer and Windows store thumbprint.

## Lines 281-288
- Comments describe auto signer and activation steps.

## Lines 289-296
- Continues code signing comments about pfx signer usage.

## Lines 297-304
- Comments describe Windows store thumbprint signer option.

## Lines 305-312
- Comments describe auto signer selection and activation.

## Lines 313-320
- Calls register_code_signers and registers exe/resources/install targets.

## Lines 321-326
- Registers MSI target, resolves targets, and ends file.
