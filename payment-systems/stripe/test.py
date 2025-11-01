#!/usr/bin/env python3
import json
import sys
from typing import Any, Dict, Optional, List

import requests

BASE_URL = "http://localhost:5051"
HEADERS = {"content-type": "application/json"}


class ApiError(Exception):
    pass


def post_json(session: requests.Session, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    url = f"{BASE_URL}{path}"
    try:
        resp = session.post(url, headers=HEADERS, json=payload, timeout=30)
    except requests.RequestException as e:
        raise ApiError(f"Request failed: {e}") from e

    ct = resp.headers.get("content-type", "")
    if resp.status_code >= 400:
        try:
            data = resp.json() if "application/json" in ct else {"_body": resp.text}
        except Exception:
            data = {"_body": resp.text}
        raise ApiError(f"HTTP {resp.status_code} on {path}: {json.dumps(data, indent=2)}")

    if "application/json" not in ct:
        raise ApiError(f"Expected JSON but got '{ct}' from {path}: {resp.text[:200]}")
    return resp.json()


def get_json(session: requests.Session, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
    url = f"{BASE_URL}{path}"
    try:
        resp = session.get(url, headers=HEADERS, params=params, timeout=30)
    except requests.RequestException as e:
        raise ApiError(f"Request failed: {e}") from e

    ct = resp.headers.get("content-type", "")
    if resp.status_code >= 400:
        try:
            data = resp.json() if "application/json" in ct else {"_body": resp.text}
        except Exception:
            data = {"_body": resp.text}
        raise ApiError(f"HTTP {resp.status_code} on {path}: {json.dumps(data, indent=2)}")

    if "application/json" not in ct:
        raise ApiError(f"Expected JSON but got '{ct}' from {path}: {resp.text[:200]}")
    return resp.json()


def pretty(label: str, obj: Dict[str, Any]) -> None:
    print(f"\n=== {label} ===")
    print(json.dumps(obj, indent=2))


# -------- API wrappers (match server.py) --------
def create_manual_pi(session: requests.Session, amount_major: float, currency: str, order_id: str) -> Dict[str, Any]:
    payload = {"amount_major": amount_major, "currency": currency, "order_id": order_id}
    return post_json(session, "/api/pi/new_manual", payload)


def confirm_pi(session: requests.Session, pi_id: str) -> Dict[str, Any]:
    # returns {"payment_intent":{"id","status","charges":[...]}}
    return post_json(session, "/api/pi/confirm", {"pi_id": pi_id})


def capture_pi(session: requests.Session, pi_id: str, amount_to_capture_minor: Optional[int]) -> Dict[str, Any]:
    # returns {"payment_intent":{"id","status"}}
    payload = {"pi_id": pi_id}
    if amount_to_capture_minor is not None:
        payload["amount_to_capture"] = amount_to_capture_minor
    return post_json(session, "/api/pi/capture", payload)


def cancel_pi(session: requests.Session, pi_id: str) -> Dict[str, Any]:
    return post_json(session, "/api/pi/cancel", {"pi_id": pi_id})


def get_pi(session: requests.Session, pi_id: str) -> Dict[str, Any]:
    # returns {"payment_intent": <full object from backend.get_payment_intent>}
    return get_json(session, "/api/pi/get", {"pi_id": pi_id})


def refund_charge(session: requests.Session, charge_id: str, amount_minor: Optional[int]) -> Dict[str, Any]:
    # returns {"refund":{"id","status","amount"}}
    payload = {"charge_id": charge_id, "amount_minor": amount_minor}
    return post_json(session, "/api/refund", payload)


def create_customer(session: requests.Session, email: str) -> Dict[str, Any]:
    # returns {"customer":{"id","email"}}
    return post_json(session, "/api/cust/new", {"email": email})


def attach_payment_method(session: requests.Session, customer_id: str, pm_id: str) -> Dict[str, Any]:
    # returns {"payment_method":{"id"}}
    return post_json(session, "/api/cust/attach_pm", {"customer_id": customer_id, "pm_id": pm_id})


def offsession_charge(session: requests.Session, customer_id: str, amount_major: float, currency: str, order_id: str) -> Dict[str, Any]:
    # returns {"payment_intent":{"id","status"}}
    payload = {"customer_id": customer_id, "amount_major": amount_major, "currency": currency, "order_id": order_id}
    return post_json(session, "/api/offsession/charge", payload)


# -------- Helpers --------
def _pluck_charge_ids_from_confirm(confirm_resp: Dict[str, Any]) -> List[str]:
    """
    Server confirm response shape:
      {"payment_intent": {"id": "...", "status": "...", "charges": [ { "id": "ch_...", ... }, ... ]}}
    """
    pi = confirm_resp.get("payment_intent") or {}
    charges = pi.get("charges") or []
    ids = []
    if isinstance(charges, list):
        for ch in charges:
            if isinstance(ch, dict) and isinstance(ch.get("id"), str):
                ids.append(ch["id"])
    return ids


def _pluck_latest_charge_from_pi(pi_obj: Dict[str, Any]) -> Optional[str]:
    """
    Try common shapes on the PI fetched via /api/pi/get:
      - payment_intent["latest_charge"] == "ch_..."
      - payment_intent["latest_charge"] == {"id": "ch_..."}
      - payment_intent["charges"] == [{"id": "ch_..."}]
    """
    latest = pi_obj.get("latest_charge")
    if isinstance(latest, str):
        return latest
    if isinstance(latest, dict) and isinstance(latest.get("id"), str):
        return latest["id"]

    charges = pi_obj.get("charges")
    if isinstance(charges, list):
        for ch in charges:
            if isinstance(ch, dict) and isinstance(ch.get("id"), str):
                return ch["id"]

    return None


def main() -> None:
    session = requests.Session()

    # ---------- Flow 1: Manual PI (auth/capture/refund) ----------
    try:
        pi_new = create_manual_pi(session, amount_major=50.00, currency="usd", order_id="ord_hold_1")
        pretty("Create manual PI", pi_new)

        pi_id = (pi_new.get("payment_intent") or {}).get("id")
        if not isinstance(pi_id, str):
            raise ApiError("Could not find payment intent id in /api/pi/new_manual response at payment_intent.id")

        pi_confirm = confirm_pi(session, pi_id)
        pretty("Confirm (authorize)", pi_confirm)

        # Try to learn the charge id from confirm (it includes 'charges')
        charge_ids = _pluck_charge_ids_from_confirm(pi_confirm)
        charge_id_from_confirm = charge_ids[0] if charge_ids else None

        # Partial capture $30.00 -> 3000 minor units
        pi_capture = capture_pi(session, pi_id, amount_to_capture_minor=3000)
        pretty("Capture partial ($30.00)", pi_capture)

        # If we didn’t get a charge id earlier (or want to be 100% sure), re-fetch PI
        charge_id = charge_id_from_confirm
        if not charge_id:
            pi_full = get_pi(session, pi_id)
            pretty("Get PI (post-capture)", pi_full)
            pi_obj = pi_full.get("payment_intent") or {}
            charge_id = _pluck_latest_charge_from_pi(pi_obj)

        if not charge_id:
            print("\n!!! Could not determine charge_id to refund. Check 'payment_intent.latest_charge' "
                  "or 'payment_intent.charges' shape from /api/pi/get and update the pluckers.")
        else:
            # Refund $5.00 -> 500 minor units
            refund = refund_charge(session, charge_id=charge_id, amount_minor=500)
            pretty("Refund ($5.00)", refund)

    except ApiError as e:
        print(f"\n[Manual PI flow error] {e}", file=sys.stderr)

    # ---------- Flow 2: Customer + off-session charge ----------
    try:
        cust = create_customer(session, email="learner@example.com")
        pretty("Create customer", cust)

        customer = cust.get("customer") or {}
        customer_id = customer.get("id")
        if not isinstance(customer_id, str):
            raise ApiError("Could not find customer id in /api/cust/new response at customer.id")

        attach = attach_payment_method(session, customer_id=customer_id, pm_id="pm_card_visa")
        pretty("Attach test payment method (default)", attach)

        # Optionally assert PM id present
        pm = attach.get("payment_method") or {}
        if not isinstance(pm.get("id"), str):
            raise ApiError("Attach PM returned no payment_method.id")

        off = offsession_charge(session, customer_id=customer_id, amount_major=9.99, currency="usd", order_id="ord_off_1")
        pretty("Off-session charge ($9.99)", off)

    except ApiError as e:
        print(f"\n[Customer/off-session flow error] {e}", file=sys.stderr)


if __name__ == "__main__":
    main()