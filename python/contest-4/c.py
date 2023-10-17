import sys

def triangular_numbers(number):
    temp = 1
    counter = 1
    while counter < number + 1:
        yield temp
        temp += counter + 1
        counter += 1

exec(sys.stdin.read())