data = [0] * 257

def perms(x):
    if 1 <= x <= 97:
        return x + 159
    if 98 <= x <= 131:
        return x + 28
    if 132 <= x <= 256:
        return x - 131
    

counter = 0
print("$$1 ", end="")
a, b = 1, perms(1)
while b != 1:
    print("\\xrightarrow{" + str(counter) + "}", b, end=" ")
    a, b = b, perms(b)
    counter += 1
print("$$", counter)
    

