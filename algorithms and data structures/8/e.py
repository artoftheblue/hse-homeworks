deque = []
size = 0

a = input().strip()

while a != "exit":
    data = tuple(a.split())
    command = data[0]
    
    if command == "push_front":
        deque.insert(0, int(data[1]))
        size += 1
        print("ok")
    elif command == "push_back":
        deque.append(int(data[1]))
        size += 1
        print("ok")
    elif command == "pop_front":
        if size != 0:
            print(deque.pop(0))
            size -= 1
        else:
            print("error")
    elif command == "pop_back":
        if size != 0:
            print(deque.pop())
            size -= 1
        else:
            print("error")
    elif command == "front":
        if size != 0:
            print(deque[0])
        else:
            print("error")
    elif command == "back":
        if size != 0:
            print(deque[-1])
        else:
            print("error")
    elif command == "size":
        print(size)
    elif command == "clear":
        deque = []
        size = 0
        print("ok")
        
    a = input().strip()

print("bye")