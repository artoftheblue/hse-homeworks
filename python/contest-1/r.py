a = int(input())
s, c = 0, 0
while a != 0:
    s += a
    c += 1
    a = int(input())
print(s / c)