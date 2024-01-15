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
        if size != 0:
            print(queue.pop())
            size -= 1
        else:
            print("error")
    elif command == "front":
        if size != 0:
            print(queue[-1])
        else:
            print("error")
    elif command == "size":
        print(size)
    elif command == "clear":
        queue = []
        size = 0
        print("ok")
        
    a = input().strip()

print("bye")