# DFS 메소드 정의
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = '')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [] # 그래프를 표현하는 인접 리스트(2차원 리스트)
visited = [] # 각 노드가 방문된 정보를 표현하는 1차원 리스트

dfs(graph, 1, visited) # dfs 함수 호출
