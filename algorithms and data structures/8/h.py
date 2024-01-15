a = input()
stack = []
size = 0

opening = "([{"
closing = ")]}"

flag = True
for i in a:
    if i in opening:
        stack.append(i)
        size += 1
    elif i in closing:
        if size == 0:
            print("no")
            flag = False
            break
        bracket = stack.pop()
        size -= 1
        if opening.index(bracket) != closing.index(i):
            print("no")
            flag = False
            break

if size != 0 and flag:
    print("no")
    flag = False

if flag:
    print("yes")
