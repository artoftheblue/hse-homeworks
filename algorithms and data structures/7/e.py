n, m = [int(x) for x in input().split()]
w = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    ci, wi = c[i - 1], w[i - 1]
    for j in range(m + 1):
        dp[i][j] = dp[i - 1][j]
        if not (w[i - 1] > j):
            dp[i][j] = max(dp[i - 1][j - wi] + ci,
                           dp[i][j])

#print(*dp, sep="\n")
a, b = n, dp[-1].index(max(dp[-1]))
#print(a, b)

answer = ""
while a > -1 and b > -1:
    #print(a, b)
    if dp[a - 1][b] == dp[a][b]:
        a -= 1
        continue
    answer = str(a) + "\n" + answer
    a -= 1
    b -= w[a]
print(answer.strip())
    