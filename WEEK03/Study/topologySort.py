from collections import deque

def topological_sort(n, edges):
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    # 그래프 구성 및 진입 차수 계산
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # 진입 차수 0인 노드 큐에 삽입
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) == n:
        return result
    else:
        return []  # 사이클 존재

# 예시 실행
edges = [(1, 3), (2, 3), (3, 4)]
print(topological_sort(4, edges))  # [1, 2, 3, 4] 또는 [2, 1, 3, 4]