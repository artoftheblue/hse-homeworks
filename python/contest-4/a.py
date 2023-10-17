import sys

def square_fibonacci(number):
    yield 1
    if number > 1:
        yield 1
    number1, number2 = 1, 1
    counter = 2
    while counter < number:
        number1, number2 = number2, number1 + number2
        yield number2 ** 2
        counter += 1

exec(sys.stdin.read())
