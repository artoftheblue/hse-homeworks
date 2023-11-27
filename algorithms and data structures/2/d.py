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

def gcd_extended(b: int, a: int) -> int: 
    if a == 0: 
        return b, 1, 0
             
    gcd, d, c = gcd_extended(a, b % a) 
    return gcd, c, d - (b // a) * c

def get_inverse(a: int) -> int:
    gcd, z, _ = gcd_extended(a, MOD)
    
    if gcd == 1:
        return -1
    return z % MOD

def main(a: int, n: int) -> int:
    gcd, x, _ = gcd_extended(a, MOD)
    
    if gcd != 1:
        return -1
    
    result = 0
    temp1 = sum(x, MOD)
    temp2 = temp1
    
    for i in range(1, n + 1):
        result = sum(result, mul(i, temp1))
        temp1 = mul(temp1, temp2)
    return result

a, n, MOD = map(int, input().split())
print(main(a, n))