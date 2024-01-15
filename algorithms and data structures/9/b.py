n, q = map(int, input().split()) 
sz = 300
arr = [0] * n 
blocks = [0] * (n // sz + 1)
for i in range(q): 
    line = input().split()
    if line[0] == 'A': 
        index = int(line[1]) - 1
        value = int(line[2])
        blocks[index // sz] += value - arr[index]
        arr[index] = value 
    else: 
        left = int(line[1]) - 1
        right = int(line[2]) - 1
        s = 0 
        while left <= right: 
            if left // sz == right // sz or left % sz != 0: 
                s += arr[left]
                left += 1
            else: 
                s += blocks[left // sz]
                left += sz
        print(s)