import heapq

heap = []
heapq.heapify(heap)

with open(r'input.txt', 'r', encoding="utf-8") as f:
    for line in f:
        if line.strip() == "CLEAR":
            heap = []
            heapq.heapify(heap)
        elif line.startswith("ADD"):
            heapq.heappush(heap, -int(line[4:]))
            #print(heap)
        elif line.strip() == "EXTRACT":
            try:
                item = heapq.heappop(heap)
                print(-item)
            except IndexError:
                print("CANNOT")
                continue