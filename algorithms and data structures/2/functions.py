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
        return a * power(a, n - 1)
    return power(a * a, n // 2)
    