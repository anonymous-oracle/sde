def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Extended Euclidean Algorithm.
    Returns a tuple (gcd, x, y) such that gcd is the greatest common divisor of a and b,
    and x and y are the coefficients satisfying the equation: a*x + b*y = gcd.
    """
    if b==0:
        return (a, 1, 0)

    r, q = a%b, a//b
    g, x1, y1 = extended_gcd(b, r)
    x = y1
    y = x1 - q * y1
    return (g, x, y)
