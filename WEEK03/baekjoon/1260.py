import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 입력 처리
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 노드 번호가 작은 것부터 방문하기 위해 정렬
for i in range(1, n+1):
    graph[i].sort()

# DFS 실행
visited = [False] * (n+1)
dfs(graph, v, visited)
print()

# BFS 실행
visited = [False] * (n+1)
bfs(graph, v, visited)