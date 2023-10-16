with open("input.txt", "r") as f:
    data = f.readlines()
bank = {}

for line in data:
    op = line.split()

    if op[0] == "BALANCE":
        if op[1] not in bank:
            print("ERROR")
        else:
            print(bank[op[1]])
    elif op[0] == "DEPOSIT":
        if op[1] not in bank:
            bank[op[1]] = int(op[2])
        else:
            bank[op[1]] += int(op[2])
    elif op[0] == "WITHDRAW":
        if op[1] not in bank:
            bank[op[1]] = -int(op[2])
        else:
            bank[op[1]] -= int(op[2])
    elif op[0] == "TRANSFER":
        if op[1] not in bank:
            bank[op[1]] = -int(op[3])
        else:
            bank[op[1]] -= int(op[3])
        if op[2] not in bank:
            bank[op[2]] = int(op[3])
        else:
            bank[op[2]] += int(op[3])
    elif op[0] == "INCOME":
        for client in bank:
            if bank[client] > 0:
                bank[client] = int(bank[client] * (1 + int(op[1]) / 100))
