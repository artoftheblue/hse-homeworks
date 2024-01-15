def first_wins(a, b) -> bool:
    if a == 9 and b == 0:
        return False
    if a == 0 and b == 9:
        return True
    return a > b

def game(first: list, size1: int, second: list, size2: int) -> str:
    for i in range(10 ** 6):
        if size1 == 0:
            return "second", i
        if size2 == 0:
            return "first", i
        
        a, b = first.pop(), second.pop()
        size1 -= 1
        size2 -= 1
        
        if first_wins(a, b):
            pointer = first
            size1 += 2
        else:
            pointer = second
            size2 += 2
        
        pointer.insert(0, a)
        pointer.insert(0, b)
    
    return "botva"

first = list(map(int, input().split()))[::-1]
second = list(map(int, input().split()))[::-1]

print(*game(first, 5, second, 5))