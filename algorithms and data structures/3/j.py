n, l = map(int, input().split())
w = [int(i) for i in input().split()]
w = [w[i] * l + i for i in range(len(w))]
ans = 0
def merge(a, b):
    global ans
    c = []
    i = j = 0
    while i != len(a) or j != len(b):
        if i == len(a):
            c += b
            break
        if j == len(b):
            c += a
            break
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            ans += len(a) - i
            c.append(b[j])
            j += 1
    return c

def sort_merge(a):
    if len(a) < 2:
        return a
    mid = len(a) // 2
    return merge(sort_merge(a[:mid]), sort_merge(a[mid:]))
print(w)
sort_merge(w)
print(ans)