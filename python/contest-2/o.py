line = input().split() + ["X"]
count = 0
while True:
    current_item = ""
    start_index = 0
    for i in range(len(line) - 2):
        if line[i] == line[i + 1] == line[i + 2]:
            start_index = i
            current_item = line[i]
            break
    if current_item != "":
        end_index = start_index
        while line[end_index] == current_item:
            end_index += 1
            count += 1
    else:
        break

    line = line[:start_index] + line[end_index:]
    #print(line)
print(count)
    
