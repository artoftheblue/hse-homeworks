n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

#print(*matrix,sep="\n")

data = [[0 for i in range(m + 1)] for j in range(n + 1)]

#print(*data,sep="\n")

for i in range(m + 1):
    data[0][i] = 1000000000000

for i in range(n + 1):
    data[i][0] = 1000000000000

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == j == 1:
            data[i][j] = matrix[i-1][j-1]
        else:
            data[i][j] = matrix[i-1][j-1] + min(data[i-1][j], data[i][j-1])

#print(*data, sep="\n")
print(data[n][m])

'''
5 4
1 1 1 1
3 100 100 100
1 1 1 1
2 2 2 2
1 1 1 1
'''