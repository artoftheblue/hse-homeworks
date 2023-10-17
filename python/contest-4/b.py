import sys

def factorials(number):
    yield 1
    temp = 1
    counter = 1
    while counter < number:
        temp *= (counter + 1)
        yield temp
        counter += 1

exec(sys.stdin.read())