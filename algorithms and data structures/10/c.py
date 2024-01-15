import heapq

n = int(input())
heap = [int(char) for char in input().split()]

heapq.heapify(heap)

total = 0
for _ in range(n - 1):
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    temp = a + b
    total += 0.05 * temp
    heapq.heappush(heap, temp)

print(f"{total:.2f}")
    
    