array = list(map(int, input().split()))
length = len(array)
count = 0
for i in range(length):
    for j in range(i + 1, length):
        if array[i] == array[j]:
            count += 1
print(count)
