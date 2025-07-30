# 다익스트라 알고리즘 이용
import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

# 최단 거리 저장할 리스트 정의
distances = [INF] * (n+1)

# m개의 버스 정보 입력
for _ in range(m):
    start, arrive, cost = map(int, input().split())
    # 단방향 그래프
    graph[start].append((arrive, cost))

# 다익스트라 구현
def dijkstra(start):
    queue = []
    # 시작 도시 최단 거리 0
    heapq.heappush(queue, (0, start))
    distances[start] = 0

    # 큐가 빌때까지 반복
    while queue:
        # 값이 가장 작은 도시 선택
        distance, city = heapq.heappop(queue)
        # 방문한 적이 있는 도시면 무시
        if distances[city] < distance:
            continue

        for next_city, cost in graph[city]:
            new_distance = distance + cost

            if new_distance < distances[next_city]:
                distances[next_city] = new_distance
                heapq.heappush(queue, (new_distance, next_city))

a, b = map(int, input().split())
# 다익스트라 수행
dijkstra(a)

# b 최단 거리 출력
print(distances[b])
