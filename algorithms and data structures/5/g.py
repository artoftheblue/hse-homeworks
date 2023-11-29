def toll_booth_ladder(n: int, args: list) -> int:
    args.insert(0, 0)
    array = [0] * (n + 1)
    for i in range(1, n + 1):
        array[i] = min(array[i - 1], array[i - 2]) + args[i]
    
    return array[-1]
    
print(toll_booth_ladder(int(input()), list(map(int, input().split()))))
