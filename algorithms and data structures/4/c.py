def bisect_find_right(item: int, array: list, length: int) -> str:
    left, right = 0, length
    while left < right:
        mid = (right + left) // 2
        if array[mid] <= item:
            left = mid + 1
        elif array[mid] > item:
            right = mid
    return right - 1

def bisect_find_left(item: int, array: list, length: int) -> str:
    left, right = 0, length
    while left < right:
        mid = (right + left) // 2
        if array[mid] < item:
            left = mid + 1
        elif array[mid] >= item:
            right = mid
    return left

def find_number_of_elements(array: list, length: int, left: int, right: int) -> int:
    return bisect_find_right(right, array, length) - \
           bisect_find_left(left, array, length) + 1

n = int(input())
array1 = list(map(int, input().split()))
array1.sort()

for _ in range(int(input())):
    left, right = map(int, input().split())
    print(find_number_of_elements(array1, n, left, right), end=" ")