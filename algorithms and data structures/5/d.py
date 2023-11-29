def what_the_fuck(n: int):
    if n in [0, 1]:
        return 1
    if n % 2 == 0:
        return what_the_fuck(n // 2) + 1
    return what_the_fuck(n + 1) + what_the_fuck((n - 1) // 2)

def weirdass_sequence(n: int) -> int:
    array = [0] * (n + 2)
    array[0] = array[1] = 1
    for i in range(1, n // 2 + 1):
        array[2 * i] = array[i] + 1
        array[2 * i + 2] = array[2 * i + 1] - array[2 * i] + 1

    #print(array)
    return array[n]

print(what_the_fuck(int(input())))
