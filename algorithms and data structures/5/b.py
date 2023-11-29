def stairballs(n: int) -> int:
    array = [0] * (n + 3)
    array[n] = 1
    for i in range(n - 1, -1, -1):
        array[i] = array[i + 1] + array[i + 2] + array[i + 3]
    
    return(array[0])
    
print(stairballs(int(input())))