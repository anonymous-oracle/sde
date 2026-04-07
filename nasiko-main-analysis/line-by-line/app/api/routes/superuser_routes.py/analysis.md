# superuser_routes.py — line-by-line analysis

## Lines 1-8
- Module docstring for superuser-only endpoints.
- Imports APIRouter, HTTPException, Depends, handler factory, types, auth dependency, httpx, os, logging.

## Lines 9-16
- Sets logger and AUTH_SERVICE_URL default.
- Defines create_superuser_routes factory and router.

## Lines 17-24
- Declares POST /user/register endpoint with response model.
- register_user accepts UserRegistrationRequest and get_super_user dependency.

## Lines 25-32
- Starts try block; builds registration payload.
- Calls auth service /auth/users/register.

## Lines 33-40
- On success, reads auth response and logs registration.
- Builds UserRegistrationResponse with role and credentials.

## Lines 41-48
- Handles non-200 responses with HTTPException.
- Catches request errors and returns 503.

## Lines 49-56
- Handles generic errors and returns 500.
- Returns router.
