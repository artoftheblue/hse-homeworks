n = int(input())
dictionary = {}
for _ in range(n):
    a, b = input().split()
    dictionary[a] = b
    dictionary[b] = a
print(dictionary[input()])
