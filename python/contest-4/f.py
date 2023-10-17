import sys

def babylonian_sequence(a):
    prev = 1
    while abs(prev ** 2 - a) > 1e-7:
        yield prev
        prev = 0.5 * (prev + a / prev)

exec(sys.stdin.read())