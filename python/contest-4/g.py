import sys
def binary_sequences(a):
    for i in range(0, 2 ** a):
        yield bin(i)[2:].zfill(a)

exec(sys.stdin.read())