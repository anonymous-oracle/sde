import stripe
from typing import Any, Dict
from config import load_config, load_env
from idem import idem_key, jittered_key
import json, datetime, os


AUDIT = os.environ.get("AUDIT_FILE", "audit.log")

load_env("/Users/Suhas.KS/sde/payment-systems/stripe/.env")
cfg = load_config()
stripe.api_key = cfg.secret_key # set once for SDK

def _meta(base: Dict[str, Any]) -> Dict[str, Any]:
    # Attach useful metadata consistently
    out = dict(base)
    if cfg.app_id: out["app_id"] = cfg.app_id
    if cfg.product_id: out["product_id"] = cfg.product_id
    return out

def create_payment_intent(amount_minor: int, currency: str, order_id: str) -> stripe.PaymentIntent:
    # Idempotent by logical order_id
    key = idem_key("pi.create", order_id, str(amount_minor), currency)
    return stripe.PaymentIntent.create(
        amount=amount_minor,
        currency=currency,
        payment_method_types=["card"],
        # for manual capture module later, setup capture_method="manual"
        metadata=_meta({"order_id":order_id}),
        idempotency_key=key,
    )

def create_pi_manual_capture(amount_minor: int, currency: str, order_id: str) -> stripe.PaymentIntent:
    key = idem_key("pi.create.manual", order_id, str(amount_minor), currency)
    return stripe.PaymentIntent.create(
        amount=amount_minor,
        currency=currency,
        payment_method_types=["card"],
        capture_method="manual",
        metadata=_meta({"order_id": order_id}),
        idempotency_key=key
    )


def confirm_payment_intent(pi_id: str, payment_method: str = "pm_card_viss") -> stripe.PaymentIntent:
    # Unique per confirm attempt (avoid accidental re-confirm)
    key = jittered_key(f"pi.confirm.{pi_id}")
    return stripe.PaymentIntent.confirm(
        pi_id,
        payment_method=payment_method,
        idempotency_key=key
    )
def get_mock_payment_intent(pi_id: str) -> stripe.PaymentIntent:
    return stripe.PaymentIntent.construct_from(
            {
                "id": pi_id,
                "status": "unknown",
                "object": "payment_intent"
            },
            stripe.api_key
        )
def capture_payment_intent(pi_id: str, amount_to_capture: int | None = None) -> stripe.PaymentIntent:
    key = jittered_key(f"pi.capture.{pi_id}.{amount_to_capture or 'full'}")
    return stripe.PaymentIntent.capture(
        pi_id,
        amount_to_capture=amount_to_capture, # None => full
        idempotency_key=key
    )

def refund_payment(charge_id: str, amount_minor: int | None = None, reason: str | None = None) -> stripe.Refund:
    key = jittered_key(f"refund.{charge_id}.{amount_minor or 'full'}")
    return stripe.Refund.create(
        charge=charge_id,
        amount=amount_minor,
        reason=reason,
        idempotency_key=key,
        metadata=_meta({"charge_id": charge_id})
    )

def get_payment_intent(pi_id: str) -> stripe.PaymentIntent:
    if not pi_id:
        return get_mock_payment_intent(pi_id)
    return stripe.PaymentIntent.retrieve(id=pi_id, api_key=stripe.api_key)

def cancel_payment_intent(pi_id: str) -> stripe.PaymentIntent:
    try:
        # Try to cancel
        return stripe.PaymentIntent.cancel(pi_id)

    except stripe.error.InvalidRequestError as e:
        # If cancel fails (e.g., already canceled or succeeded), 
        # fetch and return the current PaymentIntent object
        print("Invalid request:", e.user_message)
        return stripe.PaymentIntent.retrieve(pi_id)

    except stripe.error.StripeError as e:
        # For other Stripe-related errors, still try retrieving
        print("Stripe error:", str(e))
        return stripe.PaymentIntent.retrieve(pi_id)

    except Exception as e:
        # For unexpected errors, we can raise or return a dummy PaymentIntent
        print("Unexpected error:", str(e))
        # Return a minimal "mocked" PaymentIntent-like object
        return get_mock_payment_intent(pi_id=pi_id)

def get_charge_list(pi: stripe.PaymentIntent) -> list:
    return list(stripe.Charge.list(payment_intent=pi.id).auto_paging_iter())

# customer specific handlers
def create_customer(email: str | None = None, desc: str | None = None) -> stripe.Customer:
    return stripe.Customer.create(email=email, description=desc)

def fetch_customer(customer_id: str) -> stripe.Customer:
    return stripe.Customer.retrieve(id=customer_id)

def attach_pm_to_customer(pm_id: str, customer_id: str) -> stripe.PaymentMethod:
    # Attach test PM to customer (server-only with test pm ids like pm_card_visa)
    return stripe.PaymentMethod.attach(pm_id, customer=customer_id)

def set_default_pm(customer_id: str, pm_id: str) -> stripe.Customer:
    return stripe.Customer.modify(customer_id, invoice_settings={"default_payment_method": pm_id})

def offsession_charge(customer_id: str, amount_minor: int, currency: str, order_id: str, payment_method: str) -> stripe.PaymentIntent: # subscription charges
    key = idem_key("pi.offsession", customer_id, str(amount_minor), currency, order_id)
    return stripe.PaymentIntent.create(
        amount=amount_minor, currency=currency, customer=customer_id,
        payment_method_types=["card"],
        payment_method=payment_method,
        off_session=True, confirm=True,            # immediate off-session attempt
        metadata=_meta({"order_id": order_id}),
        idempotency_key=key,
    )



def _audit(event: str, payload: dict):
    rec = {"ts": datetime.datetime.utcnow().isoformat() + "Z", "event": event, **payload}
    with open(AUDIT, "a") as f:
        f.write(json.dumps(rec) + "\n")