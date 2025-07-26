import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()

for i in range(1, n+1):
    queue.append(i)
    
while True:
    if len(queue) == 1:
        break
    else:
        queue.popleft()
        x = queue[0]
        queue.popleft()
        queue.append(x)
        
print(queue[0])