int(input())
a = sorted([int(x) for x in input().split()])
input()
b = sorted([int(x) for x in input().split()])
int(input())
c = sorted([int(x) for x in input().split()])
input()
d = sorted([int(x) for x in input().split()])
i = j = k = l = 0
ami = 0
bmj = 0
cmk = 0
dml = 0
m = max(a[0], b[0], c[0], d[0]) - min(a[0], b[0], c[0], d[0])
while i != len(a) and j != len(b) and k != len(c) and l != len(d):
    print(i, j, k, l, "\n", ami, bmj, cmk, dml)
    if m > max(a[i], b[j], c[k], d[l]) - min(a[i], b[j], c[k], d[l]):
        m = max(a[i], b[j], c[k], d[l]) - min(a[i], b[j], c[k], d[l])
        ami = i
        bmj = j
        cmk = k
        dml = l
    if max(a[i], b[j], c[k], d[l]) - min(a[i], b[j], c[k], d[l]) == 0:
        break
    elif min(a[i], b[j], c[k], d[l]) == a[i]:
        i += 1
    elif min(a[i], b[j], c[k], d[l]) == b[j]:
        j += 1
    elif min(a[i], b[j], c[k], d[l]) == c[k]:
        k += 1
    elif min(a[i], b[j], c[k], d[l]) == d[l]:
        l += 1
print(a[ami], b[bmj], c[cmk], d[dml])