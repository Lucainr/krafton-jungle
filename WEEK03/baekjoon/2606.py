import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    queue = deque()
    count = 0
    queue.append(1)
    visited[1] = True
    while queue:
        current = queue.popleft()
        for value in graph[current]:  # enumerate 제거 (불필요)
            if visited[value] == False:
                queue.append(value)
                visited[value] = True  # True 할당 추가
                count += 1
    print(count)

visited = [False for _ in range(n+1)]
bfs()