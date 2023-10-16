array = list(map(int, input().split()))
min_item = 99999999999999
for item in array:
    if item % 2 == 1 and item < min_item:
        min_item = item
print(min_item)
# returning