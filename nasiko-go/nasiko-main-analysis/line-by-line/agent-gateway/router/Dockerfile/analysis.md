# Dockerfile — line-by-line analysis

## Lines 1-8
- Uses Python 3.12 slim, sets workdir, includes commented apt-get deps.

## Lines 9-16
- Copies router project and installs Poetry with no venvs.

## Lines 17-24
- Exposes port 8000 and runs uvicorn for router app with reload.
