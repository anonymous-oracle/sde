# BINARY_BUILD_GUIDE.md — line-by-line analysis

## Lines 1-8
- Introduces the binary build guide and starts the quick comparison table.

## Lines 9-16
- Lists comparison rows for size, interpreter, run speed, offline, complexity, maintenance, and cross-compilation.

## Lines 17-24
- Adds "best for" row, starts architecture section, and lists Linux targets.

## Lines 25-32
- Lists macOS/Windows targets, notes no cross-compilation, and starts current binary info.

## Lines 33-40
- Describes current binary details and opens PyInstaller method section.

## Lines 41-48
- Explains PyInstaller and shows prerequisite install commands.

## Lines 49-56
- Starts build process section with pyinstaller build command.

## Lines 57-64
- Notes output location and begins binary test commands.

## Lines 65-72
- Finishes test commands and starts distribution instructions.

## Lines 73-80
- Shows packaging steps and opens spec file configuration section.

## Lines 81-88
- Lists spec file settings and introduces PyApp method.

## Lines 89-96
- Describes PyApp and shows prerequisite build steps.

## Lines 97-104
- Builds distribution wheel with uv and notes output.

## Lines 105-112
- Starts embedded PyApp build block and setup commands.

## Lines 113-120
- Lists PyApp build environment variables and cargo build.

## Lines 121-128
- Notes binary output, copies it, and starts multi-platform section.

## Lines 129-136
- Begins build environment setup and lists Linux x86_64 requirements.

## Lines 137-144
- Lists Linux ARM64 and macOS Intel build environment requirements.

## Lines 145-152
- Lists macOS ARM and Windows build requirements, closes block.

## Lines 153-160
- Starts GitHub Actions build matrix example with workflow header.

## Lines 161-168
- Defines tag trigger, job, matrix structure, and include list.

## Lines 169-176
- Adds matrix entries for Linux x64/arm and macOS Intel.

## Lines 177-184
- Adds macOS ARM and Windows matrix entries and closes include.

## Lines 185-192
- Sets runs-on/steps and installs uv in the workflow.

## Lines 193-200
- Shows PyInstaller build step and starts artifact upload step.

## Lines 201-208
- Completes artifact upload config and starts naming convention section.

## Lines 209-216
- Provides naming pattern and example artifact names.

## Lines 217-224
- Ends naming section and opens troubleshooting for missing modules.

## Lines 225-232
- Shows hiddenimports snippet and starts runtime import error issue.

## Lines 233-240
- Shows datas snippet for runtime import errors.

## Lines 241-248
- Lists solutions for oversized binaries.

## Lines 249-256
- Notes PyApp wheel error workaround and starts performance section.

## Lines 257-264
- Shows startup time table and opens memory usage section.

## Lines 265-272
- Shows memory usage table and starts recommendation section.

## Lines 273-280
- Lists PyInstaller recommendation reasons for Nasiko CLI.

## Lines 281-288
- Lists PyApp use cases and starts version management section.

## Lines 289-296
- Shows version update instruction and explains automatic updates list.

## Lines 297-304
- Lists version impact outputs and begins current status summary.

## Lines 305-310
- Completes status section with PyInstaller details and PyApp issue note.
