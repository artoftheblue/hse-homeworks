import sys

def sum_of_digits(n: int):
    return sum([int(digit) for digit in str(abs(n))])

exec(sys.stdin.read())
