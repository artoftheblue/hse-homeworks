def binary_search(left: int, right: int, help_array: list, main_array: list) -> int:
    while left < right:
        mid = (left + right) // 2
        if main_array[help_array[mid]] >= main_array[i]:
            right = mid
        else:
            left = mid + 1
    
    return left

def generate_sequence(n: int, a1: int, k: int, b: int, m: int) -> list:
    array = []
    prev = a1
    for _ in range(1, n + 1):
        array.append(prev)
        prev = (k * prev + b) % m
    
    return array
    
n, a1, k, b, m = map(int, input().split())
x = generate_sequence(n, a1, k, b, m)

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

s = [0] * saved_index
k = m[saved_index]
for j in range(saved_index - 1, -1, -1):
    s[j] = x[k]
    k = p[k]

print(len(s))