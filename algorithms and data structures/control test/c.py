def lorries(n: int, k: int) -> int:
    stacks = [n]
    
    while True:
        temp = []
        for i in stacks:
            if i > k:
                temp.append(i // 2)
                temp.append(i // 2 + i % 2)
            else:
                temp.append(i)
        stacks = temp.copy()
        print(stacks)
        if all(i <= k for i in temp):
            return len(stacks)

n, k = map(int, input().split())
print(lorries(n, k))