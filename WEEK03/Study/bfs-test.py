from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    print(f"초기 상태: queue={list(queue)}, visited={visited}")

    while queue:
        v = queue.popleft()
        print(f"\n➡️ {v} 방문 (큐에서 꺼냄)")
        print(f"현재 queue={list(queue)}")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                print(f"  ↳ {i} 추가 -> queue={list(queue)}")

# 그래프와 visited 초기화
graph = [
    [],
    [2, 4],
    [1, 3],
    [2, 4],
    [1, 3]
]
visited = [False] * 5

bfs(graph, 1, visited)