def required_days(a, k, b, m):
    return lambda x: (x - x // k) * a + (x - x // m) * b

def binary_search(func, left: int, right: int, x: int) -> int:
    while right - left > 1:
        mid = (right + left) // 2
        #print(left, func(mid), right)
        if func(mid) >= x:
            right = mid
        else:
            left = mid

    return right

a, k, b, m, x = map(int, input().split())

print(binary_search(required_days(a, k, b, m), 0, max(a, b) * x, x))