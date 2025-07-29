import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)