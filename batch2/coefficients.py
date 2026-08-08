def horners_method(coefficients, w):
    if len(coefficients) <= 0:
        return 0
    if len(coefficients) == 1:
        return coefficients[0]
    
    result = coefficients[0]
    for idx in range(1, len(coefficients)):
        result = result * w + coefficients[idx]
    return result

if __name__ == "__main__":
    coeffs = [1, 0, -3, 2]
    w = 2
    print(horners_method(coeffs, w))