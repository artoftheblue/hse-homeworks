n, k = list(map(int, input().split()))
data = {}
for _ in range(k):
    number, word = input().split()
    data[word] = int(number)
counts = [0] * n
for key in data:
    counts[data[key] - 1] += 1
print(*counts)
