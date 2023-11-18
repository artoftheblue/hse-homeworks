def generate_primes(num):
    array = [True for _ in range(num + 1)]
    array[0], array[1] = False, False
    
    for i in range(2, int((num + 1) ** 0.5) + 1):
        if array[i]:
            j = i ** 2 
            while j < num + 1:
                array[j] = False
                j += i
                
    
    primes = []
    
    for i in range(num + 1):
        if array[i] == True:
            primes.append(i)
    
    return primes

PRIMES = generate_primes(2000001)

def main(*reqs: int):
    array = []
    
    for req in reqs:
        array.append(PRIMES[req - 1])
         
    return array
        
_ = int(input())
print(*main(*map(int, input().split())))