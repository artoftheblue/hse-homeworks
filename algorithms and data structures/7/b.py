n = int(input())
w = list(map(int, input().split()))

final = 9999999999999999

for mask in range(0, 2 ** n):
    sums = [0, 0]
    for j in range(n):
        sums[(mask >> j) & 1] += w[j]
    final = min(final, abs(sums[0] - sums[1]))

print(final)
