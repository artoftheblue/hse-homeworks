n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

for i in a:
    if i in b:
        print(i, end=" ")
        b.remove(i)
        
