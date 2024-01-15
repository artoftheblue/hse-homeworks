n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
matrix = [[0 for i in range(m)] for j in range(n)]

matrix[0][0] = data[0][0]

for i in range(1, n):
    matrix[i][0] = data[i][0] + matrix[i-1][0]

for i in range(1, m):
    matrix[0][i] = data[0][i] + matrix[0][i-1]

for i in range(1, n):
    for j in range(1, m):
        matrix[i][j] = data[i][j] + max(matrix[i-1][j], matrix[i][j-1])

print(matrix[-1][-1])