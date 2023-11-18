def is_prime(n: int):
    if n == 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True
        

def get_factors(n: int, prime=False):
    array = []
    
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            array.extend(set((i, n // i)))
   
    array.sort()
    return array

def get_prime_count(array: list):
    counter = 0
    
    for number in array:
        if is_prime(number):
            counter += 1
    
    return counter

def main(n: int):
    array = []
    
    for i in range(2, n + 1):
        if get_prime_count(get_factors(i)) >= 3:
            array.append(i)
    
    return array

print(*main(int(input())))
        