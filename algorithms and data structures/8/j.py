from collections import deque

def countingSort(arr, exp, deq, negative):
    n = len(arr)
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp if not negative else -(-arr[i] // exp))
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n-1, -1, -1):
        index = (arr[i] // exp if not negative else -(-arr[i] // exp))
        deq[count[index % 10] - 1].append(arr[i])
        count[index % 10] -= 1

    arr.clear()
    for dq in deq:
        while dq:
            arr.append(dq.popleft())

def radixSort(arr: list, n: int):
    negatives = deque([x for x in arr if x < 0])
    positives = [x for x in arr if x >= 0]

    max_positive = max(positives) if positives else 0
    max_negative = -min(negatives) if negatives else 0

    exp = 1
    deq = [deque() for _ in range(10)]

    while max_positive // exp > 0:
        countingSort(positives, exp, deq, False)
        exp *= 10

    exp = 1
    while max_negative // exp > 0:
        countingSort(negatives, exp, deq, True)
        exp *= 10

    arr[:] = [x for x in reversed(negatives)] + positives

n = int(input())
arr = list(map(int, input().split()))
radixSort(arr, n)
print(*arr)