def power(a, n):
    if n > 0:
        if n % 2 == 1:
            return (a * power(a, n - 1))
        return power(a * a, n // 2)
    if n == 0:
        return 1
    if n < 0:
        if n % 2 == 1:
            return ((1 / a) * power(a, n + 1))
        return power(1 / (a * a), n // 2)
print(power(float(input()), int(input())))
