# .dockerignore — line-by-line analysis

## Lines 1-8
- Ignores Python caches, bytecode, shared objects, and .Python marker.

## Lines 9-16
- Ignores virtual environments and env files; allows .env.example.

## Lines 17-24
- Ignores OS-specific files and IDE directories.

## Lines 25-32
- Ignores swap/backup files and test artifacts.

## Lines 33-40
- Ignores logs and temp files.
- Excludes Dockerfiles and compose files from build context.

## Lines 41-46
- Ignores uv.lock as a dev artifact in app build context.
