def calculator(n: int) -> int:
    array = [1000000000] * (n + 1)
    array_from = [0] * (n + 1)
    array[1] = 1
    
    functions = [
        lambda x: x - 1,
        lambda x: -1 if x % 2 != 0 else x // 2,
        lambda x: -1 if x % 3 != 0 else x // 3
    ]
    
    for i in range(2, n + 1):
        for func in functions:
            res = func(i)
            if res != -1:
                if array[res] + 1 < array[i]:
                    array_from[i] = res
                    array[i] = array[res] + 1
    
    string = ""
    i = n
    while i != 0:
        string = str(i) + " " + string
        i = array_from[i]
    
    print(array[-1] - 1)
    print(string)

calculator(1)