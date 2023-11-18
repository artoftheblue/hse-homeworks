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

def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def is_prime(n: int):
    if n == 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def main(a: int, n: int) -> int:
    res = 0