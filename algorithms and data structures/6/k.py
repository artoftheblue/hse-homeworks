def longest_common_increasing_subsequence(array1: list, length1: int, array2: list, length2: int) -> int:
    array = [0] * m
 
    for elem1 in range(length1):
        temp = 0
        for elem2 in range(length2):
            if array1[elem1] == array2[elem2]:
                if temp + 1 > array[elem2]:
                    array[elem2] = temp + 1
 
            if array1[elem1] > array2[elem2]:
                if array[elem2] > temp:
                    temp = array[elem2]
 
    result = 0
    for i in range(length2):
        if array[i] > result:
            result = array[i]
 
    return result

n, m = map(int, input().split())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

print(longest_common_increasing_subsequence(array1, n, array2, m))