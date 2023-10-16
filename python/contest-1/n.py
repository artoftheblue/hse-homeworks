a, b, c, d = [int(input()) for _ in range(4)]
if a == b == 0:
    print("INF")
elif b * c == a * d or a == 0:
    print("NO")
elif b % a == 0:
    x = b // a * (-1)
    print(x)
else:
    print("NO")
