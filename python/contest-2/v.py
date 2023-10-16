array1 = set(input().split())
array2 = set(input().split())
count = 0
for number in array1:
    if number in array2:
        count += 1
print(count)
