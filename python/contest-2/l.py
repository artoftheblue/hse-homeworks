array = list(map(int, input().split()))
print(*([array[-1]] + array[:-1]))