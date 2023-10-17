n, k = int(input()), int(input())

def C(n, k):
    if k == 0 or n == k:
        return 1
    return C(n - 1, k - 1) + C(n - 1, k)

print(C(n, k))
