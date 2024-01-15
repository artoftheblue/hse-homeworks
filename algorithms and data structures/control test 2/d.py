n, k = [int(i) for i in input().split()]
grasshopper = [0 for i in range(n)]

grasshopper[0] = 1

l = int(input())
frogs = []
if l != 0:
    frogs = list(map(int, input().split()))
for frog in frogs:
    grasshopper[frog - 1] = -1

for i in range(1, n):
    for j in range(1, k + 1):
        if i - j < 0 or grasshopper[i] == -1:
            pass
        else:
            if grasshopper[i - j] != -1:
                grasshopper[i] += grasshopper[i - j]

print(grasshopper[-1])