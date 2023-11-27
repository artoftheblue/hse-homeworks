x = int(input())

j2, j3 = 1, 1
i2, i3 = 1, 1
last = 0
i = 1
while True:
    if i2 == i3:
        last = i2
        j2 += 1
        j3 += 1
        i2, i3 = j2 ** 2, j3 ** 3
    elif i2 < i3:
        last = i2
        j2 += 1
        i2 = j2 ** 2
    elif i2 > i3:
        last = i3
        j3 += 1
        i3 = j3 ** 3
    if i == x:
        print(last)
        break
    i += 1