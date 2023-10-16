import sys

def add_list(ls: list, v: int):
    ls[:] = [v + item for item in ls]

exec(sys.stdin.read())
