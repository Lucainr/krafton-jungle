import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
time = 0
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        cx, cy = q.popleft()
        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    visited[cx][cy] += 1
                if visited[nx][ny] == 0 and graph[nx][ny] != 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

while True:
    count = 0
    visited = [[0]*m for _ in range(n)]

    # 덩어리 탐색
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and graph[i][j] > 0:
                bfs(i, j)
                count += 1

    # 🔍 디버깅 출력: 현재 해, 덩어리 수, visited 배열
    print(f"\n[Year {time}] 덩어리 수 = {count}")
    print("visited 배열 (주변 바다 개수+1):")
    for row in visited:
        print(row)
    print("graph 현재 상태:")
    for row in graph:
        print(row)

    # 종료 조건
    if count >= 2:
        print(f"\n빙산이 분리됨 → 정답: {time}")
        break
    if count == 0:
        print("\n모든 빙산이 녹음 → 정답: 0")
        break

    # 빙산 녹이기
    for i in range(n):
        for j in range(m):
            if visited[i][j] != 0:
                graph[i][j] -= (visited[i][j] - 1)
                if graph[i][j] < 0:
                    graph[i][j] = 0

    time += 1