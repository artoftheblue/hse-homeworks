array = list(map(int, input().split()))
for i in range(len(array) - 1):
    if array[i] / abs(array[i]) == array[i + 1] / abs(array[i + 1]):
        print(array[i], array[i + 1])
        break
