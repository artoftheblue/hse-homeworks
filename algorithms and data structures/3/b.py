def counting_sort(*data):
    helper_pos = [0] * 10001
    helper_neg = [0] * 10001

    for i in data:
        if i >= 0:
            helper_pos[i] += 1
        else:
            helper_neg[i] += 1
    
    array = []
    for i in range(-10000, 0, 1):
        while helper_neg[i] > 0:
            array.append(i)
            helper_neg[i] -= 1
    
    for i in range(0, 10001, 1):
        while helper_pos[i] > 0:
            array.append(i)
            helper_pos[i] -= 1
    
    return array

_ = int(input())
print(*counting_sort(*map(int, input().split())))