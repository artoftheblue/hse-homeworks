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

MOD = 1000000007

def main(a: int, b: int, c: int, d: int):
    res = div(sum(mul(a, d), mul(b, c)), mul(b, d))
    return res

print(main(*map(int, input().split())))