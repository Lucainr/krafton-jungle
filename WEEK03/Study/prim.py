import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]  # (weight, vertex)
    total_weight = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        total_weight += weight

        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v))

    return total_weight

# 인접 리스트로 표현된 그래프
graph = {
    'A': [('B', 2), ('D', 6)],
    'B': [('A', 2), ('C', 3), ('D', 8)],
    'C': [('B', 3), ('E', 7)],
    'D': [('A', 6), ('B', 8), ('E', 5)],
    'E': [('C', 7), ('D', 5)]
}

print("MST 최소 가중치 합:", prim(graph, 'A'))  # 결과: 17