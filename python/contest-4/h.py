import sys

def generate_sequences(a, n):
    for i in range(0, n ** a):
        res = ""
        for j in range(0, a):
            res = str(i // (n ** j) % n) + res
        yield res

exec(sys.stdin.read())
