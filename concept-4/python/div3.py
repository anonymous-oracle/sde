def check_divisibility(num: int = 0, div: int = 1):
    if div == 0:
        return False
    return num % div == 0

for i in range(1, 22):
    if check_divisibility(i, 3):
        print(i)