MOD = 1000003
a = int(input())

result = 1
for i in range(2, min(MOD + 1, a + 1)):
    result *= i
    result %= MOD

print(result)