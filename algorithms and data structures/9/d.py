from math import ceil

f = open(r"input.txt", "r")
n = int(f.readline())
array = [int(char) for char in f.readline().split()]

block_size = round(n ** 0.5)
#print(block_size)
block_count = ceil(n / block_size)
blocks = [0] * block_count
indexes = [0] * block_count

def fill_block(function):
    for i in range(block_count):
        subarray = array[block_size * i:block_size * (i + 1)]
        blocks[i] = function(subarray)
        indexes[i] = subarray.index(blocks[i])
        
func = max
fill_block(func)
temp_indexes = [indexes[i] + i * block_size for i in range(len(indexes))]
#print(blocks, temp_indexes)

#print(blocks, indexes)

k = int(f.readline())

for req in range(k):
    #print("\n\niter")
    l, r = map(int, f.readline().split())
    #print("BEGIN", l, r)
    l, r = l - 1, r - 1
    next_l, prev_r = l // block_size + 1, r // block_size - 1
    check = blocks[next_l:prev_r + 1]
    #print("A", next_l, prev_r, check)
    total = 0
    block_index = -1
    
    if check != []:
        total = func(check)
        ind = check.index(total)
        #print(ind, indexes)
        block_index = temp_indexes[next_l + ind]
    
    #print(next_l, prev_r, check, total)
    
    thing_a = array[l:min(next_l * block_size, r + 1)]
    thing_b = array[max((prev_r + 1) * block_size, l):r + 1]
    
    max_a = max(thing_a)
    index_a = l + thing_a.index(max_a)
    
    max_b = max(thing_b)
    index_b = max((prev_r + 1) * block_size, l) + thing_b.index(max_b)
    
    data = [(total, -block_index), (max_a, -index_a), (max_b, -index_b)]
    data.sort(reverse=True)
    #print(data)
    #print(data)
    print(-data[0][1] + 1, end=" ")