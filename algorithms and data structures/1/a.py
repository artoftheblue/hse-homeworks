def get_divisors(n: int):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n

print(get_divisors(int(input())))