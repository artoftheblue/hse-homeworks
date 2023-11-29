def is_prime(n: int):
    if n == 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def get_min_divisor(n: int):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and is_prime(i):
            return i

n = int(input())
sum_counter = 0
for i in range(3, n + 1):
    if not is_prime(i):
        sum_counter += get_min_divisor(i)

print(sum_counter)