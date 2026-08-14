def euclidean_gcd(a,b):
    if b==0:
        return a
    print(a,b)
    return euclidean_gcd(b, a % b)
if __name__ == "__main__":
    a, b = 252, 105
    euclidean_gcd(a, b) 