n = int(input())
array = [input().split()[0] for _ in range(n)]
print(len(set(array)))