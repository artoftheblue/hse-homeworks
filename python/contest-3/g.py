def distance(x1, y1, x2, y2):
    return abs((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

x1, y1, x2, y2, x3, y3 = [float(input()) for _ in range(6)]
print(round(distance(x1, y1, x2, y2) + distance(x1, y1, x3, y3) + distance(x2, y2, x3, y3), 6))
