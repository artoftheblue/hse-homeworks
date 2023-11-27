def get_validate_cosmis_settlement_function(a: int, b: int, w: int, h: int):
    return lambda x: validate_cosmic_settlement(a, b, w, h, x)

def validate_cosmic_settlement(a: int, b: int, w: int, h: int, x: int):
    size_a, size_b = a + 2 * x, b + 2 * x
    metric_a, metric_b = (w // size_a) * (h // size_b), (h // size_a) * (w // size_b)
    return max(metric_a, metric_b)


def binary_search(func, left: int, right: int, n: int) -> int:
    while right - left > 1:
        mid = (right + left) // 2
        if func(mid) >= n:
            left = mid 
        else:
            right = mid

    return left

n, a, b, w, h = map(int, input().split())
print(binary_search(get_validate_cosmis_settlement_function(a, b, w, h), 0, min(w, h), n))
