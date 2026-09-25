# n8n.py — line-by-line analysis

## Lines 1-8
- Module docstring and imports typer/Optional/Rich console helpers.

## Lines 9-16
- Imports API client/endpoints, initializes console, starts register_workflow.

## Lines 17-24
- Defines register_workflow args/docstring and prints status messages.

## Lines 25-32
- Builds API client/payload and sets optional agent name.

## Lines 33-40
- Adds agent description, posts register request, handles response.

## Lines 41-48
- Prints success details including agent name/id/webhook/upload.

## Lines 49-56
- Prints failure message and raises Exit on error.

## Lines 57-64
- Handles exceptions and starts connect_n8n signature.

## Lines 65-72
- Builds payload for N8N connection and posts connect request.

## Lines 73-80
- Parses response data and checks connection status.

## Lines 81-88
- Prints success info or reports connection failure.

## Lines 89-96
- Handles exceptions and starts get_n8n_credentials.

## Lines 97-104
- Fetches credentials endpoint and handles response validation.

## Lines 105-112
- Extracts credential data and builds status string.

## Lines 113-120
- Builds credential info text with last_tested/created_at fields.

## Lines 121-128
- Adds updated_at info and prints panel or no-credentials message.

## Lines 129-136
- Handles errors and starts update_n8n_credentials signature.

## Lines 137-144
- Validates at least one field provided and begins payload build.

## Lines 145-152
- Adds payload fields and sends update request.

## Lines 153-160
- Handles response and exceptions for update call.

## Lines 161-168
- Starts delete_n8n_credentials with confirmation prompts.

## Lines 169-176
- Confirms deletion, sends delete request, handles response.

## Lines 177-184
- Handles delete errors and starts list_n8n_workflows.

## Lines 185-192
- Builds request params and calls workflows endpoint.

## Lines 193-200
- Parses workflows list and total count.

## Lines 201-208
- Prints workflows heading and iterates workflow entries.

## Lines 209-216
- Builds workflow info string with active/chat/nodes/updated/tags.

## Lines 217-224
- Prints workflow info or no workflows message.

## Lines 225-232
- Handles exceptions for workflows listing.

## Lines 233-240
- Continues workflow info formatting and tag rendering.

## Lines 241-248
- Completes list_n8n_workflows output handling.

## Lines 249-251
- Handles final exception and exits on errors.
