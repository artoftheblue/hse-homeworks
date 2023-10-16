import sys

def check(a: list, b: list):
    set1, set2 = set(a), set(b)
    flag = True
    for item in set1:
        if item not in set2:
            flag = False
    for item in set2:
        if item not in set1:
            flag = False
    return flag * 1

exec(sys.stdin.read())
