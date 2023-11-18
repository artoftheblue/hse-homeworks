def gcd(a: int, b: int):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
a, b = int(input()), int(input())
print(a * b // gcd(a, b))