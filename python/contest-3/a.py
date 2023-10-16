import sys

def mul_list(ls: list, v: int):
    ls[:] = [v * item for item in ls]

exec(sys.stdin.read())
