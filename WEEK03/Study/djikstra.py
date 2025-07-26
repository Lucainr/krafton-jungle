import heapq  # 우선순위 큐 사용

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # 무한대로 초기화
    distances[start] = 0  # 시작 노드는 거리 0
    queue = [(0, start)]  # (거리, 노드)

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)

        if cur_dist > distances[cur_node]:
            continue  # 이미 더 짧은 거리로 방문한 경우

        for neighbor, weight in graph[cur_node]:
            distance = cur_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

graph = {
    1: [(2, 2), (3, 5)],
    2: [(3, 1), (4, 2)],
    3: [(5, 3)],
    4: [(5, 1)],
    5: []
}

result = dijkstra(graph, 1)
print(result)