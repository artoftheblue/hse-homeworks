def IsPointInArea(x, y):
    return ((x + 1) ** 2 + (y - 1) ** 2 <= 4) and (y >= 2 * x + 2) and (y >= -x) or ((x + 1) ** 2 + (y - 1) ** 2 >= 4) and (y <= 2 * x + 2) and (y <= -x)        

if IsPointInArea(*[float(input()) for _ in range(2)]):
    print("YES")
else:
    print("NO")
