n = int(input())
array = list(map(int, input().split()))

while True:
    c_min = min(array)
    c_max = max(array)
    if c_min == c_max:
        break
    index = array.index(c_max)
    array[index] -= c_min

print(array[0])