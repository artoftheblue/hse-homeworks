n = int(input())
queue = []
size = 0

for _ in range(n):
    command = input().strip().split()
    
    if command[0] == "-":
        print(queue.pop(0))
        size -= 1
    elif command[0] == "+":
        queue.append(int(command[1]))
        size += 1
    elif command[0] == "*":
        queue.insert((size + 1) // 2, int(command[1]))
        size += 1
    