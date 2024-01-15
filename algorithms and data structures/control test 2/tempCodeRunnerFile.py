from math import ceil
n = int(input())
data = (list(range(1, 10)) + [0]) * ceil(n / 10)
data = data[:n]
array = [0 for _ in range(n + 2)]

print(data, array)

for i in range(2, n + 2):
    array[i] = min(data[i - 1], data[i - 2])

print(array) 