def xor(x, y):
    return ((x and not y) or (not x and y)) * 1

print(xor(int(input()), int(input())))
