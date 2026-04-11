# superuser-init.yaml — line-by-line analysis

## Lines 1-8
- ConfigMap header for superuser init script and script key.

## Lines 9-16
- Shell script setup, defaults, and log message.

## Lines 17-24
- Calls auth service to create superuser and captures HTTP response.

## Lines 25-32
- Extracts HTTP code/body and prints status.

## Lines 33-40
- On success, extracts credentials and prints headers.

## Lines 41-48
- Prints credential details and reads service account token.

## Lines 49-56
- Builds secret JSON and starts create secret request.

## Lines 57-64
- Sends create secret request and captures HTTP code.

## Lines 65-72
- Handles secret created or starts update flow on conflict.

## Lines 73-80
- Sends update request and reports update status.

## Lines 81-88
- Handles create failure and starts 400 error handling.

## Lines 89-96
- Handles already-exists error or bad request response.

## Lines 97-104
- Handles generic failure and starts Job definition.

## Lines 105-112
- Job metadata with Helm hook annotations.

## Lines 113-120
- Job spec with backoff, service account, and initContainers start.

## Lines 121-128
- Wait-for-auth init container command and loop start.

## Lines 129-136
- Wait loop completion or timeout exit.

## Lines 137-144
- Main container setup with env vars and command.

## Lines 145-152
- Mounts script configMap and defines volume.

## Lines 153-155
- Sets configMap name and defaultMode.
