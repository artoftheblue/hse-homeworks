n = int(input())
 
a = []
stack = []
length = [0]

def iter():
    data = input()
    if data == "-":
        stack.pop()
        length[0] -= 1
        return a.pop()
    #print(data)
    
    number = int(data[1:])
    if data[0] == "+":
        a.append(number)
        if length[0] != 0:
            length[0] += 1
            stack.append(stack[-1] + number)
        else:
            stack.append(number)
            length[0] += 1
        return 
    
    if number == 1:
        return a[-1]
    if number == length[0]:
        return stack[-1]
    return stack[-1] - stack[len(stack) - number - 1]

for _ in range(n):
    ans = iter()
    if ans != None:
        print(ans)