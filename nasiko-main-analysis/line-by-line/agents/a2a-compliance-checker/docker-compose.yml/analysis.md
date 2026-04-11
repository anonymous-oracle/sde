# docker-compose.yml — line-by-line analysis

## Lines 1-8
- Defines a2a-compliance-checker service with build, container name, and env vars.

## Lines 9-16
- Sets stdin/ports/tty, attaches to agents-net and agents-db-net networks.

## Lines 17-22
- Declares external networks for agents and database.
