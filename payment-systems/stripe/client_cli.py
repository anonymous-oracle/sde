# client_cli.py
import sys, requests, json

BASE = "http://127.0.0.1:5051"

def create_pi(amount_major: float, currency: str, order_id: str):
    r = requests.post(f"{BASE}/api/pi/new", json={"amount_major": amount_major, "currency": currency, "order_id": order_id})
    print(json.dumps(r.json(), indent=2))
    return r.json()["payment_intent"]["id"]

def confirm_pi(pi_id: str):
    r = requests.post(f"{BASE}/api/pi/confirm", json={"pi_id": pi_id})
    print(json.dumps(r.json(), indent=2))

if __name__ == "__main__":
    # Usage:
    # python client_cli.py on_session 12.99 usd ord_1001
    cmd = sys.argv[1]
    if cmd == "on_session":
        _, _, amt, cur, order = sys.argv
        pi_id = create_pi(float(amt), cur, order)
        confirm_pi(pi_id)


