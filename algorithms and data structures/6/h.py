def weirdass_longest_increasing_subsequence(array: list, n: int) -> int:
    dp = [1] * n
 
    for i in range(1, n):
        for j in range(0, i):
            #print(array[i], array[j])
            if dp[i] < dp[j] + 1 and array[i] % array[j] == 0:
                dp[i] = dp[j] + 1

    return max(dp)
 
n = int(input())
array = list(map(int, input().split()))
print(weirdass_longest_increasing_subsequence(array, n))