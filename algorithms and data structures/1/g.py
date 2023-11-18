def generate_sum(num):
    summa = 0
    
    array = [True for _ in range(num + 1)]
    array[0], array[1] = False, False
    
    for i in range(2, int((num + 1) ** 0.5) + 1):
        if array[i]:
            j = i ** 2 
            #print("a", j, i, num, summa)
            while j <= num:
                if array[j]:
                    summa += i
                    array[j] = False
                j += i
                #print("b", j, i, summa)
                
    primes = []
    
    for i in range(num + 1):
        if array[i]:
            primes.append(i)

    #print(primes, sum(primes))
    
    return sum(primes) + summa

print(generate_sum(int(input())))