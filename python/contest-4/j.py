import sys

def factorial(a):
    if a < 0:
        return "FactorialCalculateError"
    temp = 1
    if a == 0:
        return temp
    for i in range(2, a + 1):
        temp *= i
    return temp

exec(sys.stdin.read())
