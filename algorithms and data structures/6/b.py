n = int(input())
matrix = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    matrix[0][i] = 1
    matrix[i][0] = 1

for i in range(1, n):
    for j in range(1, n):
        matrix[j][i] = matrix[j][i - 1] + matrix[j - 1][i]

for i in range(n):
    k, j = 0, i
    while j != -1:
        print(matrix[k][j], end=" ")
        k += 1
        j -= 1
    print()
    
    
    