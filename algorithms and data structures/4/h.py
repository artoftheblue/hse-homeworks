def cows_count(distance: int, array: list, length: int):
    cow_counter = 1
    prev = 0
    
    for i in range(1, length):
        current_cow = array[i]
        previous_cow = array[prev]
        if current_cow - previous_cow > distance:
            cow_counter += 1
            prev = i    
    
    return cow_counter

def get_cows_count_function(array, length):
    return lambda x: cows_count(x, array, length)

def binary_search(func, left: int, right: int, k: int) -> int:
    while right - left > 0:
        mid = (right + left) // 2
        if func(mid) >= k:
            left = mid + 1
        else:
            right = mid

    return left


n, k = map(int, input().split())
array = list(map(int, input().split()))

print(binary_search(get_cows_count_function(array, n), 0, array[-1], k))