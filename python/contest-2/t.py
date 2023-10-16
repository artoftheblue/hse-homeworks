with open("input.txt", "r") as f:
    data = f.read().split()

dictionary = {}
for word in data:
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1

max_count = 0
max_word = ""
for word in dictionary:
    if dictionary[word] > max_count:
        max_count = dictionary[word]
        max_word = word
    if dictionary[word] == max_count and word < max_word:
        max_word = word
print(max_word)
