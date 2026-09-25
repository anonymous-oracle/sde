# Dockerfile — line-by-line analysis

## Lines 1-8
- Uses Python 3.11 slim, installs curl, and cleans apt cache.

## Lines 9-16
- Copies requirements, installs deps, and copies application code.

## Lines 17-24
- Sets PYTHONPATH/UNBUFFERED env and defines HTTP healthcheck.

## Lines 25-26
- Runs registry service via registry.py.
