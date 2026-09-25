# A shipping company's cost function isn't given to you — derive it yourself from this policy: packages under 2kg cost a flat $5. From 2kg up to and including 10kg, cost is $5 plus $1.50 per kg over 2kg. Above 10kg, cost is a flat $20. First, write out f(weight) explicitly as a 3-piece piecewise function on paper/in a comment — state each piece's exact domain boundary and whether each boundary is open or closed. Then implement it as a Python function. Then write pytest table tests covering: a normal case in each of the 3 pieces, both boundary weights (2kg and 10kg) checked against whichever piece's rule actually owns that exact point, and a negative-weight input that should raise ValueError. All tests must pass.

def shipping_cost(weight):
    if weight < 0:
        raise ValueError("Weight cannot be negative")
    if weight < 2:
        return 5
    elif weight <= 10:
        return 5 + 1.5 * (weight - 2)
    else:
        return 20