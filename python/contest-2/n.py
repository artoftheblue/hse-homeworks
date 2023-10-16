n, k = list(map(int, input().split()))
kegels = ["I"] * n
for _ in range(k):
    a, b = list(map(int, input().split()))
    for i in range(a - 1, b):
        kegels[i] = "."
print("".join(kegels))
