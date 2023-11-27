def ropes_count(array: list):
    return lambda x: sum(item // x for item in array)

def binary_search(func, left: int, right: int, k: int) -> int:
    while right - left > 1:
        mid = (right + left) // 2
        if func(mid) < k:
            right = mid
        else:
            left = mid

    return left

n, k = map(int, input().split())
ropes = [int(input()) for _ in range(n)]

print(binary_search(ropes_count(ropes), 0, 10 ** 8, k))