# 1) Create manual PI
curl -s localhost:5051/api/pi/new_manual -H 'content-type: application/json' -d '{"amount_major": 50.00, "currency":"usd", "order_id":"ord_hold_1"}' | jq

# 2) Confirm to authorize (places an auth hold on the card)
curl -s localhost:5051/api/pi/confirm -H 'content-type: application/json' -d '{"pi_id":"<the-pi-id-from-step-1>"}' | jq

# 3a) Capture partial, say $30.00
curl -s localhost:5051/api/pi/capture -H 'content-type: application/json' -d '{"pi_id":"<the-pi-id>", "amount_to_capture":3000}' | jq

# 3b) Or cancel the auth instead (optional endpoint you can add later)
curl -s localhost:5051/api/pi/cancel -H 'content-type: application/json' -d '{"pi_id":"<the-pi-id>"}' | jq

# Suppose charge id = ch_123
curl -s localhost:5051/api/refund -H 'content-type: application/json' -d '{"charge_id":"ch_123", "amount_minor":500}' | jq   # $5.00

# 1) Make a customer
curl -s localhost:5051/api/cust/new -H 'content-type: application/json' \
  -d '{"email":"learner@example.com"}' | jq

# 2) Attach a test payment method & set as default
curl -s localhost:5051/api/cust/attach_pm -H 'content-type: application/json' \
  -d '{"customer_id":"cus_...", "pm_id":"pm_card_visa"}' | jq

# 3) Charge later (off-session)
curl -s localhost:5051/api/offsession/charge -H 'content-type: application/json' \
  -d '{"customer_id":"cus_...","amount_major":9.99,"currency":"usd","order_id":"ord_off_1"}' | jq

# If you switch pm_id to pm_card_chargeCustomerFail, you can test off-session failure paths (e.g., expired card) and see payment_intent.status and last_payment_error.