with open("input.txt", "r") as f:
    filedata = f.readlines()

data = {}
for line in filedata:
    surname, item, quantity = line.split()
    quantity = int(quantity)
    if surname not in data:
        data[surname] = {}
        data[surname][item] = quantity
    else:
        if item not in data[surname]:
            data[surname][item] = quantity
        else:
            data[surname][item] += quantity

data = dict(sorted(data.items()))
for key in data:
    print(key + ":")
    for key2 in dict(sorted(data[key].items())):
        print(key2, data[key][key2])
        
