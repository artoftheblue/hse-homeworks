fib = [0, 1]
for i in range(50):
    fib.append(fib[i] + fib[i + 1])

x = int(input())
if x in fib:
    print(fib.index(x))
else:
    print(-1)
