import sys 
from collections import deque

def push_front(dq, x):
    dq.appendleft(x)
    print("ok")

def push_back(dq, x):
    dq.append(x)
    print("ok")

def pop_front(dq):
    if size(sq) != 0:
        print(dq.popleft())
    else:
        print("error")

def pop_back(dq):
    if size(sq) != 0:
        print(dq.pop())
    else:
        print("error")
        
def front(dq):
    return dq[0]

def size(dq):
    return len(dq)

def back(dq):
    return dq[size(dq) - 1]

def clear(dq):
    dq.clear()
    return dq

def exit():
    print("bye")
    sys.exit()
    
dq = deque()
push_back(dq, 1)
print(back(dq))
exit()
