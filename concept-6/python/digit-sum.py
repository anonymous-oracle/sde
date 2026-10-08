def sum_digits(num: int):
    if num // 10 == 0 or num < 0:
        return num
    return sum_digits(num // 10) + num % 10

print(sum_digits(4093))
print(sum_digits(80791))
