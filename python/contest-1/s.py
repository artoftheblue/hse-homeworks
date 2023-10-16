n = int(input())
x = float(input())
s = float(input())
for i in range(n):
    s *= x
    s += float(input())

print(s)
