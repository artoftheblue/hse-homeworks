from sys import setrecursionlimit

setrecursionlimit(9999999)

def power(a, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(a, -n)
    return a * power(a, n - 1)
print(power(float(input()), int(input())))