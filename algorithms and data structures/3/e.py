def merge(a: list, n: int, b: list, m: int) -> list:
    pointerA, pointerB = 0, 0
    result = []
    while pointerA < n and pointerB < m:
        itemA, itemB = a[pointerA], b[pointerB]
        if itemA == itemB:
            print(itemA, end=" ")
            print(itemB, end=" ")
            pointerA += 1
            pointerB += 1
        elif itemA < itemB:
            print(itemA, end=" ")
            pointerA += 1
        elif itemA > itemB:
            print(itemB, end=" ")
            pointerB += 1
    while pointerA < n:
        print(a[pointerA], end=" ")
        pointerA += 1
    while pointerB < m:
        print(b[pointerB], end=" ")
        pointerB += 1
    return result

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

print(*merge(a, n, b, m))

