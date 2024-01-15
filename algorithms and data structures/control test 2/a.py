n = int(input())
array = [int(item) for item in input().split()]
new = [0]
counter = 0
for i in array:
    if i == 0:
        counter += 1
    new.append(counter)

#print(new)

for i in range(int(input())):
    a, b = map(int, input().split())
    print(new[b] - new[a - 1], end=" ")