MOD = 1000003

def fibonacci(n: int):
    if n == 0:
        return 0, 1

    j, k = fibonacci(n // 2)
    l, m = j * (k * 2 - j), j ** 2 + k ** 2

    return l * ((n + 1) % 2) + m * (n % 2), \
            m * ((n + 1) % 2) + (l + m) * (n % 2)

print(fibonacci(int(input()))[1] % MOD)