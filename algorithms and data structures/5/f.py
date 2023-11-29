def explosivity2_electic_boogaloo(n: int) -> int:
    array = [[] for _ in range(n + 1)]
    array[1] = (1, 2)
    for i in range(2, n + 1):
        pointer = array[i - 1]
        array[i] = [pointer[1], 2 * (pointer[0] + pointer[1])]
    
    return sum(array[n])

print(explosivity2_electic_boogaloo(int(input())))