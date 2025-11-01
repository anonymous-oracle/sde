# keys.py (extract idempotency key from Stripe responses if needed)
def maybe_idem(resp):
    # stripe-python exposes 'last_response' with headers
    last = getattr(resp, 'last_response', None)
    if last and hasattr(last, 'headers'):
        return last.headers.get('Idempotency-Key')
    return None