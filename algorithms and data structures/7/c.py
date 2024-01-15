n = int(input())
w = [0] + [int(x) for x in input().split()]
sum_w = sum(w)
m = sum(w) // 2
if sum_w % 2 == 1:
    print("NO")
else:
    dp = [[-1] * (m + 1) for i in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        wi = w[i]
        for j in range(m + 1):
            dp[i][j] = dp[i - 1][j]
            if j - wi < 0 or dp[i - 1][j-wi] == -1:
                continue
            if dp[i - 1][j - wi] == 1:
                dp[i][j] = 1
    if dp[-1][-1] == 1:
        print("YES")
    else:
        print("NO")