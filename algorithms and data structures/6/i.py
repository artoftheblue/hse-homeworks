def longest_common_subsequence(array1: list, length1: int, array2: list, length2: int) -> int:
    dp = [[0] * (length2 + 1) for _ in range(0, length1 + 1)]
 
    for i in range(0, length1 + 1):
        for j in range(0, length2 + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif array1[i - 1] == array2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
 
    print(dp[length1][length2])
    
    indexes1 = ""
    indexes2 = ""
 
    i = length1
    j = length2
    while i > 0 and j > 0:
        if array1[i - 1] == array2[j - 1]:
            indexes1 = str(i) + " " + indexes1
            indexes2 = str(j) + " " + indexes2
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
 
    print(indexes1.strip(), indexes2.strip(), sep="\n")

string1 = list(input())
string2 = list(input())
longest_common_subsequence(string1, len(string1), string2, len(string2))