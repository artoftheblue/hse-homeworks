def determine_enough_positivity(positivities: list, n: int, max_pos: int):
    if sum(positivities) < max_pos: 
        return -1
    
    min_count = n + 1
    min_index = 0
    for i in range(n):
        temp_sum = positivities[i]
        temp_count = 1
        index = (i + 1) % n
        while index != i and temp_sum < max_pos:
            temp_sum += positivities[index]
            temp_count += 1
            index = (index + 1) % n
            
        if temp_count < min_count:
            min_count = temp_count
            min_index = i
    
    return " ".join([str(min_index + 1), str(min_count)])


n, p = map(int, input().split())
positivities = list(map(int, input().split()))

print(determine_enough_positivity(positivities, n, p))