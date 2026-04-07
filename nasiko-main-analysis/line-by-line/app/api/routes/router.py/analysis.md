# router.py — line-by-line analysis

## Lines 1-8
- Module docstring for main router composition.
- Imports APIRouter and route factory functions.

## Lines 9-16
- Imports remaining route factories and HandlerFactory.
- Defines create_router signature.

## Lines 17-24
- Docstring explains combining feature routes.
- Instantiates APIRouter.

## Lines 25-32
- Includes health, registry, upload, operations, update routes.
- Adds GitHub and N8N routes.

## Lines 33-40
- Adds superuser, search, chat history, observability, and NANDA routes.

## Lines 41-43
- Returns combined router.
