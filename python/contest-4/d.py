import sys

def binomial_coefficients(number):
    temp = 1
    for i in range(1, number + 2):
        yield temp
        temp *= (number + 1 - i)
        temp //= i

exec(sys.stdin.read())