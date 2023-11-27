def bisect_find(item: int, array: list, length: int) -> str:
    left, right = 0, length - 1
    while left <= right:
        mid = (right + left) // 2
        if array[mid] < item:
            left = mid + 1
        elif array[mid] > item:
            right = mid - 1
        else:
            return "YES"
    return "NO"

n, k = map(int, input().split())
array1 = list(map(int, input().split()))


for item in array2:
    print(bisect_find(item, array1, n))