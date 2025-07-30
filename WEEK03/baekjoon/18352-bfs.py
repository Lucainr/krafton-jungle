# 1 번부터 N번까지의 도시와 Mrodml단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
# 이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확이 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오.
# 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

# 첫째 줄에 도시의 개수 N, 도로의 개수 M, 출발 도시의 번호 X가 주어진다.
# 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다.
# 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미이다.
# A, B는 서로 다른 자연수

# X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
# 이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.

import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

def bfs(start):
    answer = []
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[node] + 1
                queue.append(i)
                if distance[i] == k:
                    answer.append(i)

    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

bfs(x)