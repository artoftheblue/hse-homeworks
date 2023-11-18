def gcd(a: int, b: int):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
print(gcd(int(input()), int(input())))