def get_factor(n: int):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return n // i, i
    
    return 1, n

def factorize(n: int):
    array = []
    
    factor = get_factor(n)
    while factor[0] != 1:
        array.append(factor[1])
        factor = get_factor(factor[0])
    array.append(factor[1])
    
    return array

print(factorize(int(input())))
        