s = 1
prev = 1
for i in range(2, int(input()) + 1):
    prev *= i
    s += prev
print(s)
