n, m = map(int, input().split())

field = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
field[2][2] = 1

for i in range(2, m + 2):
    for j in range(2, n + 2):
        if i != 2 and j != 2:
            field[j][i] = field[j - 2][i - 1] + field[j - 1][i - 2]


print(field[n + 1][m + 1])
