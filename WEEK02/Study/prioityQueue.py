import heapq

# 최소 힙을 이용한 우선순위 큐
priority_queue = []
heapq.heappush(priority_queue, (2, 'task2'))
heapq.heappush(priority_queue, (1, 'task1'))
heapq.heappush(priority_queue, (3, 'task3'))

while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print(f"Processing: {task}, Priority: {priority}")