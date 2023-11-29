def explosivity(n: int) -> int:
    array = [[] for _ in range(n + 1)]
    array[1] = [['A'], ['B']]
    for i in range(2, n + 1):
        for item in array[i - 1]:
            array[i].append(item.copy() + ['B'])
            if item[-1] != 'A':
                array[i].append(item.copy() + ['A'])
    
    return len(array[n])

print(explosivity(int(input())))