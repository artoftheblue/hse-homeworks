def gcd(a: int, b: int):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def counter(x1: int, y1: int, x2: int, y2: int):
    x_length = abs(x1 - x2)
    y_length = abs(y1 - y2)
    
    if x_length == 0 or y_length == 0:
        return 1 + x_length + y_length
    
    return 1 + gcd(x_length, y_length)

print(counter(*map(int, input().split())))