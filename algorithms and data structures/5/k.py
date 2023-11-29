def strings(n: int, array: list) -> int:  
    if n == 2:
        return array[1] + array[0]
    
    lengths = [0] * n
    
    lengths[1] = array[1] - array[0]
    lengths[2] = array[2] - array[0]
    
    for i in range(3, n):
        lengths[i] = min(lengths[i - 1], lengths[i - 2]) + array[i] - array[i - 1]
    
    #print(lengths)
    return lengths[n - 1]

n = int(input())
array = list(sorted(map(int, input().split())))

print(strings(n, array))
