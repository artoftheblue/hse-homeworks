def sum(a: int, b: int) -> int:
    return (a % MOD + b % MOD) % MOD

def sub(a: int, b: int) -> int:
    return (a % MOD - b % MOD) % MOD 

def mul(a: int, b: int) -> int:
    return (a % MOD) * (b % MOD) % MOD 

def power(a: int, n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return a
    if n & 1:
        return a * power(a, n - 1) % MOD
    return power(a * a % MOD, n // 2) % MOD

def div(a: int, b: int) -> int:
    return mul(a, power(b, MOD - 2)) % MOD

def gcd_extended(a: int, b: int) -> int: 
    if a == 0 : 
        return b, 0, 1
             
    gcd, d, c = gcd_extended(b % a, a) 
    return gcd, c - (b // a) * d, d 

def get_inverse(a: int) -> int:
    gcd, z, _ = gcd_extended(a, MOD)
    #print(gcd)
    
    if gcd != 1:
        return -1
    return z % MOD

def main(a: int, n: int) -> int:
    res = 0
    for i in range(1, n + 1):
        p = power(a, i)
        inv = get_inverse(p)
        
        if inv == -1:
            return -1
        
        res = sum(res, mul(i, inv))
    return res

a, n, MOD = map(int, input().split())
print(main(a, n))