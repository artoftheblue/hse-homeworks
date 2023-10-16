array = list(map(int, input().split()))
count = 0
for item in array:
    if item > 0:
        count += 1
print(count)
