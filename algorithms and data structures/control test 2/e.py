n = int(input())

data = [[int(char) for char in input().strip()] for _ in range(n)]
matrix = [[0 for _ in range(n)] for __ in range(n)]

matrix[0][0] = data[0][0]

for i in range(1, n):
    matrix[i][0] = data[i][0] + matrix[i-1][0]
    matrix[0][i] = data[0][i] + matrix[0][i-1]    

for i in range(1, n):
    for j in range(1, n):
        matrix[i][j] = data[i][j] + min(matrix[i-1][j], matrix[i][j-1])

#print(matrix, matrix[-1][-1])

answer = [["-" for _ in range(n)] for __ in range(n)]
indexes = [n - 1, n - 1]
for i in range(n ** 2 - 1):
    a, b = indexes
    answer[a][b] = "#"
    if matrix[a - 1][b] < matrix[a][b - 1]:
        answer[a - 1][b] = "#"
        indexes[0] -= 1
    else:
        answer[a][b - 1] = "#"
        indexes[1] -= 1
    if 0 in indexes:
        break

if indexes[0] == 0:
    for i in range(indexes[1], -1, -1):
        answer[0][i] = "#"
if indexes[1] == 0:
    for i in range(indexes[0], -1, -1):
        answer[i][0] = "#"

for line in answer:
    print(*line,sep="")
    