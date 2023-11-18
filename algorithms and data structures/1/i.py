def gcd(a: int, b: int):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gears(n: int, k: int):
    return n * k // gcd(n, k)
    
print(gears(*map(int, input().split())))