import sys
sys.setrecursionlimit(10000)  # 재귀 제한 늘리기 (DFS에서 필요)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 간선 입력
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프이므로 양쪽 연결

def dfs(node):
    visited[node] = True
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)