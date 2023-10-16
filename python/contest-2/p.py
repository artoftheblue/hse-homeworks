data = []
for _ in range(8):
    data.append(tuple(map(int, input().split())))

flag = True
for i in range(8):
    for j in range(i + 1, 8):
        if data[i][0] == data[j][0] or data[i][1] == data[j][1] or \
           abs(data[i][0] - data[j][0]) == abs(data[i][1] - data[j][1]):
            flag = False
            break
    if not flag:
        break
if flag:
    print("NO")
else:
    print("YES")
