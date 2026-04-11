# kong-migrations.yaml — line-by-line analysis

## Lines 1-8
- Defines Helm hook job for Kong migrations in nasiko namespace.

## Lines 9-16
- Sets hook policies, SA, restart policy, and starts container config.

## Lines 17-24
- Runs kong migrations bootstrap with Postgres env config.

## Lines 25-29
- Sets Kong DB credentials (db/user/password).
