def IsPointInCircle(x, y, xc, yc, r):
    return ((x - xc) ** 2 + (y - yc) ** 2 <= r ** 2)

if IsPointInCircle(*[float(input()) for _ in range(5)]):
    print("YES")
else:
    print("NO")
