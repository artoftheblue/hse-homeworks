def power(a: float, n: int):
    if n == 0:
        return 1
    if n == 1:
        return a
    if n == 2:
        return a * a 
    if n % 2 == 0:
        return power(power(a, 2), n // 2)
    return a * power(a, n - 1)

print(power(float(input()), int(input())))