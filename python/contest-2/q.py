with open("input.txt", "r") as f:
    data = f.read().split()

dictionary = {}
for word in data:
    if word not in dictionary:
        print(0, end=" ")
        dictionary[word] = 1
    else:
        print(dictionary[word], end=" ")
        dictionary[word] += 1

