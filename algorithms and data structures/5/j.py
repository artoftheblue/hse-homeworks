def ticket_booth(length: int, array: list) -> int:
    time = [0] * (length + 1)
    time[1] = array[0][0]
    
    if length > 1:
        time[2] = min(array[0][0] + array[1][0],
                                    array[0][1])
    if length > 2:
        time[3] = min(time[2] + array[2][0],
                      time[1] + array[1][1],
                                array[0][2])
    if length > 3:
        for i in range(4, length + 1):
            time[i] = min(time[i - 1] + array[i - 1][0], 
                          time[i - 2] + array[i - 2][1],
                          time[i - 3] + array[i - 3][2])
    #print(time)
    return time[length]

n = int(input())
array = [tuple(map(int, input().split())) for _ in range(n)]

print(ticket_booth(n, array))