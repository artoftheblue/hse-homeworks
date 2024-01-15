n, k = [int(i) for i in input().split()]
grasshopper = [0 for i in range(n)]

grasshopper[0] = 1

for i in range(1, n):
    for j in range(1, k + 1):
        if i - j < 0:
            pass
        else:
            grasshopper[i] += grasshopper[i - j]

print(grasshopper[-1])