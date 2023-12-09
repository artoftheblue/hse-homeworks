n, m = map(int, input().split())
matrix = [[0 for i in range(n)] for j in range(m)]

for i in range(n):
    matrix[0][i] = 1
    
for i in range(m):
    matrix[i][0] = 1

for i in range(1, n):
    for j in range(1, m):
        matrix[j][i] = matrix[j][i - 1] + matrix[j - 1][i]

print(matrix[m - 1][n - 1])