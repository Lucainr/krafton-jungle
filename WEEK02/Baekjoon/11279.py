import heapq, sys

input = sys.stdin.readline

n = int(input())
max_heap = []

for i in range(n):
    number = int(input())
    
    if number > 0:
        heapq.heappush(max_heap, -number)
    else:
        if not max_heap:
            print(0)
        else:
            print(-heapq.heappop(max_heap))
            
            
            