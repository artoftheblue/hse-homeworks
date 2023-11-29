def simple_sequence(n: int) -> int:
    array = [0] * (n + 2)
    array[0] = array[1] = 1
    for i in range(1, n // 2 + 1):
        array[2 * i] += array[i] + array[i - 1]
        array[2 * i + 1] += array[i] - array[i - 1]
    
    return array[n]

print(simple_sequence(int(input())))
        