def merge(a: list, n: int, b: list, m: int) -> list:
    pointerA, pointerB = 0, 0
    result = []
    while pointerA < n and pointerB < m:
        itemA, itemB = a[pointerA], b[pointerB]
        if itemA == itemB:
            result.append(itemA)
            result.append(itemB)
            pointerA += 1
            pointerB += 1
        elif itemA < itemB:
            result.append(itemA)
            pointerA += 1
        elif itemA > itemB:
            result.append(itemB)
            pointerB += 1
    while pointerA < n:
        result.append(a[pointerA])
        pointerA += 1
    while pointerB < m:
        result.append(b[pointerB])
        pointerB += 1
    return result

def merge_sort(array: list, length: int):
    if length in [0, 1]:
        return array
    breaker = length // 2
    subbreaker = length - breaker
    return merge(merge_sort(array[:breaker], breaker), breaker, merge_sort(array[breaker:], subbreaker), subbreaker)

n = int(input())
a = list(map(int, input().split()))

print(*merge_sort(a, n))

