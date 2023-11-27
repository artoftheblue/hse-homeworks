def get_min_diff(n: int, array1: list, m: int, array2: list) -> tuple:
    pointerA, pointerB = 0, 0
    min_diff = 999999999999999999999
    diff = array1[pointerA] - array2[pointerB]
    saved_pointers = (pointerA, pointerB)
    
    while pointerA < n and pointerB < m:
        diff = abs(array1[pointerA] - array2[pointerB])
        if diff < min_diff:
            min_diff = abs(diff)
            saved_pointers = (pointerA, pointerB)
        
        if array1[pointerA] < array2[pointerB]:
            pointerA += 1
        else:
            pointerB += 1
        
    return array1[saved_pointers[0]], array2[saved_pointers[1]]

#print(get_min_diff(2, [4, 5], 3, [1, 2, 3]))
print(get_min_diff(int(input()), list(map(int, input().split())), int(input()), list(map(int, input().split()))))