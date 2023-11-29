def efficiency(x: int, time_per_baloon: int, max_count: int, break_time: int) -> int:
    cycle = time_per_baloon * max_count + break_time
    count = (x + break_time) // cycle * max_count
    remainder = max((x + break_time) % cycle - break_time, 0)
    count += remainder // time_per_baloon
    return count

def get_efficiency_function(t: int, z: int, y: int):
    return lambda x: efficiency(x, t, z, y)

def fetch_list(x: int):
    return [func(x) for func in functions]

def fetch_count(x: int) -> int:
    return sum(fetch_list(x))

m, n = map(int, input().split())
functions = [get_efficiency_function(*map(int, input().split())) for _ in range(n)]

def binary_search(func, left: int, right: int, k: int) -> int:
    last = 10 ** 9
    while right - left > 1:
        mid = (right + left) // 2
        data = func(mid)
        if data >= k:
            right = mid 
            last = mid
        else:
            left = mid

    return right, last

ans, total = binary_search(fetch_count, -1, 10 ** 9, m)
array = fetch_list(total)
array[-1] -= sum(array) - m
print(ans)
print(*array)