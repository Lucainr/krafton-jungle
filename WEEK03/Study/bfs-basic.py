from collections import deque
# BFS 메소드 정의

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end = '')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [] # 그래프를 표현하는 인접 리스트(2차원 리스트)
visited = [] # 각 노드가 방문된 정보를 표현하는 1차원 리스트

bfs(graph, 1, visited) # bfs 함수 호출