def binary_search(left: int, right: int, help_array: list, main_array: list) -> int:
    while left < right:
        mid = (left + right) // 2
        if main_array[help_array[mid]] >= main_array[i]:
            right = mid
        else:
            left = mid + 1
    
    return left

n = int(input())
x = list(map(int, input().split()))

p = [0] * n
m = [0] * (n + 1)
m[0] = -1

saved_index = 0
for i in range(0, n):
    index = binary_search(1, saved_index + 1, m, x)

    p[i] = m[index - 1]
    m[index] = i
    
    if index > saved_index:
        saved_index = index 
        
    print(p, m)

s = [0] * saved_index
k = m[saved_index]
for j in range(saved_index - 1, -1, -1):
    s[j] = x[k]
    k = p[k]

print(*s)