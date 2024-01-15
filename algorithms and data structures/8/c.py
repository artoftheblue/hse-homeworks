queue = []
size = 0

a = input().strip()

while a != "exit":
    data = tuple(a.split())
    command = data[0]
    
    if command == "push":
        queue.insert(0, int(data[1]))
        size += 1
        print("ok")
    elif command == "pop":
        print(queue.pop())
        size -= 1
    elif command == "front":
        print(queue[-1])
    elif command == "size":
        print(size)
    elif command == "clear":
        queue = []
        size = 0
        print("ok")
        
    a = input().strip()

print("bye")