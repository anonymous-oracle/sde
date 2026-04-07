# health_routes.py — line-by-line analysis

## Lines 1-8
- Module docstring for health endpoints.
- Imports APIRouter and HandlerFactory.

## Lines 9-16
- Defines create_health_routes factory.
- Creates router with Health tag and /healthcheck endpoint.

## Lines 17-22
- healthcheck delegates to handlers.health.healthcheck.
- Returns router.
