from math import ceil

n = int(input())
array = [int(char) for char in input().split()]

block_size = int(n ** 0.5)
block_count = ceil(n / block_size)
blocks = [0] * block_count

def fill_block(function):
    for i in range(block_count):
        blocks[i] = function(array[block_size * i:block_size * (i + 1)])

func = max
fill_block(func)

#print(blocks)

k = int(input())

for req in range(k):
    l, r = map(int, input().split())
    l, r = l - 1, r - 1
    next_l, prev_r = l // block_size + 1, r // block_size - 1
    check = blocks[next_l: prev_r + 1]
    total = 0
    if check != []:
        total = func(check)
    
    #print(next_l, prev_r, check, total)
    
    thing_a = array[l:min(next_l * block_size, r + 1)]
    thing_b = array[max((prev_r + 1) * block_size, l):r + 1]
    total = func(*thing_a, *thing_b, total)
    #print(thing_a, thing_b, total)
    print(array[l:r+1].index(total) + l + 1, end=" ")
    