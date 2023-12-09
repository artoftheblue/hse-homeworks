def lorries(n: int, k: int) -> int:
    stacks = [0, 0]
    stacks_count = [0, 0]
    stack = n
    
    while True:
        stacks[0] = stacks[0] // 2 
        stacks[1] = stacks[1] // 2 + stack % 2
        stacks_count[stacks[0] % 2] += stacks[0]
        stacks_count[stacks[1] % 2] += stacks[1]
        print(stacks, stacks_count)
        
        if not (stacks[0] > k and stacks[1] > k):
            return stack

n, k = map(int, input().split())
print(lorries(n, k))