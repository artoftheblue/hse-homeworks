result = [0]
    
def depth_first_search(values: list, index: int):
    length = len(values)
    if index == length:
        result[0] += 1
        return 
    
    for i in range(length):
        values[index] = i
        
        if valid(values, index):
            depth_first_search(values, index + 1)

def valid(values: list, n: int) -> bool:
    for i in range(n):
        if values[i] == values[n] or abs(values[n] - values[i]) == n - i:
            return False
    
    return True

depth_first_search([-1]*int(input()), 0)
print(result[0])