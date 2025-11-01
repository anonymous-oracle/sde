# server.py
import os, json
from flask import Flask, jsonify, request
from config import load_config, load_env
from currency import to_minor_units, is_valid_min
import backend

app = Flask(__name__)

@app.get("/health")
def health():
    return {"ok": True, "app_id": backend.cfg.app_id}

@app.post("/api/pi/new")
def api_pi_new():
    # Expect JSON: {"amount_major": 12.99, "currency": "usd", "order_id": "ord_123"}
    data = request.get_json(force=True)
    amt_minor = to_minor_units(float(data["amount_major"]), data.get("currency", backend.cfg.default_currency))
    if not is_valid_min(amt_minor, backend.cfg.min_amount_minor):
        return jsonify({"error": "amount_below_min"}), 400
    pi = backend.create_payment_intent(amt_minor, data.get("currency", backend.cfg.default_currency), data["order_id"])
    return jsonify({"payment_intent": {"id": pi.id, "status": pi.status}})

@app.post("/api/pi/confirm")
def api_pi_confirm():
    # Expect JSON: {"pi_id": "pi_xxx"}
    data = request.get_json(force=True)
    pi = backend.confirm_payment_intent(data["pi_id"], payment_method="pm_card_visa") # test-only method id
    return jsonify({"payment_intent": {"id": pi.id, "status": pi.status, "charges":  backend.get_charge_list(pi)}})

@app.post("/api/pi/new_manual")
def api_pi_new_manual():
    data = request.get_json(force=True)
    amt_minor = to_minor_units(float(data["amount_major"]), data.get("currency", backend.cfg.default_currency))
    if not is_valid_min(amt_minor, backend.cfg.min_amount_minor):
        return {"error":"amount_below_min"}, 400
    pi = backend.create_pi_manual_capture(amt_minor, data.get("currency", backend.cfg.default_currency), data["order_id"])
    return {"payment_intent": {"id": pi.id, "status": pi.status}}

@app.post("/api/pi/capture")
def api_pi_capture():
    data = request.get_json(force=True)
    pi = backend.capture_payment_intent(data["pi_id"], data.get("amount_to_capture"))
    return {"payment_intent":{"id":pi.id, "status": pi.status}}

@app.post("/api/pi/cancel")
def api_pi_cancel():
    data = request.get_json(force=True)
    pi = backend.cancel_payment_intent(data["pi_id"])
    return jsonify({"payment_intent": pi})

@app.get("/api/pi/get")
def api_pi_get():
    # Expect pi_id
    params = request.args.to_dict()
    pi = backend.get_payment_intent(params.get("pi_id"))
    return jsonify({"payment_intent": pi})

@app.post("/api/refund") # refund can only happen once the charge is captured
def api_pi_refund():
    # Expect {"charge_id":"ch_xxx", "amount_minor":null_or_int}
    data = request.get_json(force=True)
    ref = backend.refund_payment(charge_id=data["charge_id"], amount_minor=data["amount_minor"])
    # Re-fetch the PaymentIntent to view amount_refunded from charges if needed
    return jsonify({"refund": {"id": ref.id, "status":ref.status, "amount": ref.amount}})

@app.post("/api/cust/new")
def api_cust_new():
    data = request.get_json(force=True) # {"email":"x@y.com"}
    c = backend.create_customer(email=data.get("email"), desc=f"APP: {backend.cfg.app_id}")
    return {"customer": {"id": c.id, "email": c.email}}

@app.post("/api/cust/attach_pm")
def api_attach_pm():
    # {"customer_id":"cus_xxx","pm_id":"pm_card_visa"}  (test-only PM)
    data = request.get_json(force=True)
    pm = backend.attach_pm_to_customer(data["pm_id"], data["customer_id"])
    backend.set_default_pm(customer_id=data["customer_id"], pm_id=pm.id)
    return jsonify({"payment_method": {"id": pm.id}})

@app.post("/api/offsession/charge")
def api_offsession_charge():
    # {"customer_id":"cus_xxx","amount_major":9.99,"currency":"usd","order_id":"ord_off_1"}
    data = request.get_json(force=True)
    amount_major = float(data["amount_major"])
    currency = data.get("currency", backend.cfg.default_currency)
    customer_id = data.get("customer_id")
    order_id = data.get("order_id")
    amt_minor = to_minor_units(amount_major=amount_major, currency=currency)
    customer = backend.fetch_customer(customer_id=customer_id)
    payment_method = customer.invoice_settings.get("default_payment_method")
    pi = backend.offsession_charge(customer_id=customer_id, amount_minor=amt_minor, currency=currency, order_id=order_id, payment_method=payment_method)
    return jsonify({"payment_intent": {"id": pi.id, "status": pi.status}})

@app.post("/webhooks/stripe")
def webhooks_stripe():
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")
    event = None

    if backend.cfg.webhook_secret:
        # Secure mode: verify signature
        try:
            event = backend.stripe.Webhook.construct_event(payload=payload, sig_header=sig_header, secret=backend.cfg.webhook_secret)
        except Exception:
            pass
    else:
        # Dev-insecure: parse JSON without verification (OK for local learning only)
        event = request.get_json(force=True)
    
    etype = event["type"]
    data = event["data"]["object"]

    # Minimal handlers - ideally DB/audit logic goes here
    if etype == "payment_intent.succeeded":
        print(f"[WH] PI succeeded: {data['id']}")
    elif etype == "charge.refunded":
        print(f"[WH] Charge refunded: {data['id']} amount={data['amount_refunded']}")
    elif etype == "payment_intent.payment_failed":
        print(f"[WH] PI failed: {data['id']} reason={data.get('last_payment_error')}")
    else:
        print(f"[WH] Unhandled event: {etype}")

    return {"received": True}





if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", "5051")))