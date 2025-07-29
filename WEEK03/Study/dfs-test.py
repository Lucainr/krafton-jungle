def dfs(graph, v, visited):
    visited[v] = True
    print(f"➡️ {v} 방문 (visited={visited})")

    for i in graph[v]:
        if not visited[i]:
            print(f"  ↳ {v} -> {i} 이동")
            dfs(graph, i, visited)
        else:
            print(f"  ⏩ {i}는 이미 방문됨, 건너뜀")

graph = [
    [],
    [2, 4],
    [1, 3],
    [2, 4],
    [1, 3]
]
visited = [False] * 5

dfs(graph, 1, visited)