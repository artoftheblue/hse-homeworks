def get_min_diff(arrays: list, lengths: list) -> list:
    pointers = [0 for _ in range(NUMBER)]
    subarray = [array[0] for array in arrays]
    local_min = min(subarray)
    local_max = max(subarray)
    diff_min = local_max - local_min
    saved_pointers = pointers.copy()
    
    while all(pointers[i] < lengths[i] for i in range(NUMBER)):
        subarray = [arrays[i][pointers[i]] for i in range(NUMBER)]
        local_min = min(subarray)
        local_max = max(subarray)
        diff = local_max - local_min
        if diff < diff_min:
            diff_min = diff
            saved_pointers = pointers.copy()
        
        if diff <= 0:
            break
        
        for i in range(NUMBER):
            while pointers[i] < lengths[i] and local_min == arrays[i][pointers[i]]:
                pointers[i] += 1
        
    return [arrays[i][saved_pointers[i]] for i in range(4)]

lengths = []
arrays = []
NUMBER = 4
for _ in range(NUMBER):
    lengths.append(int(input()))
    arrays.append(list(sorted(list(map(int, input().split())))))

print(*get_min_diff(arrays, lengths))