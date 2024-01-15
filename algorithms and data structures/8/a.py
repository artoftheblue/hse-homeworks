a = input().strip()
stack = []
size = 0

while a != "exit":
    command = tuple(a.split())
    
    if command[0] == "size":
        print(size)
    elif command[0] == "push":
        stack.append(int(command[1]))
        size += 1
        print("ok")
    elif command[0] == "pop":
        print(stack.pop())
        size -= 1
    elif command[0] == "clear":
        stack = []
        size = 0
        print("ok")
    elif command[0] == "back":
        print(stack[-1])
    
    a = input().strip()

print("bye")