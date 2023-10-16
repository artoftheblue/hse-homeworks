array = list(map(int, input().split()))
height = int(input())
result = len(array) + 1
for i in range(len(array)):
    if height > array[i]:
        result = i + 1
        break
print(result)