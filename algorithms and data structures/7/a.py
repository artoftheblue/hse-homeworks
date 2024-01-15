m, n = [int(x) for x in input().strip().split()]
w = [0] + [int(x) for x in input().strip().split()]
c = w

dp = [[-1]*(m+1) for i in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
    ci, wi = c[i], w[i]
    for j in range(m+1):
        dp[i][j] = dp[i-1][j]
        if j - wi < 0 or dp[i-1][j-wi] == -1:
            continue
        if dp[i-1][j-wi] + ci> dp[i][j]:
            dp[i][j] = dp[i-1][j-wi] + ci
print(max(dp[-1]))