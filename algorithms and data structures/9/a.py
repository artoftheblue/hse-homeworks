n = int(input())
array = [int(char) for char in input().split()]

answer = array[0]
left = right = total = min_total = 0
min_position = -1

for i in range(n):
    total += array[i]
    
    current = total - min_total
    if current > answer:
        answer = current
        left = min_position + 1
        right = i 
    
    if total < min_total:
        min_total = total
        min_position = i

print(left + 1, right + 1, answer)