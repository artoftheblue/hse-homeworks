with open("algorithms and data structures/3/input.txt", "r", encoding="utf-8") as f:
    text = f.readlines()

data = {9: [],
        10: [],
        11: []}

for line in text:
    s = line.split()
    data[int(s[0])].append(s[1])

for index in [9, 10, 11]:
    for line in data[index]:
        print(index, line)    
