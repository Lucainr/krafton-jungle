import sys
from collections import deque

# 입력 받기
n, m = map(int, sys.stdin.readline().split())  # n: 행의 개수, m: 열의 개수
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
time = 0  # 경과 시간(년)

# 상, 하, 우, 좌 이동을 위한 방향 벡터
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def bfs(x, y):
    """
    BFS로 빙산 덩어리를 탐색하고 주변 바다 개수를 계산
    이 로직을 통해서 연결된 빙산을 하나의 덩어리로 묶고,
    동시에 해당 빙산 칸의 주변 바다 개수를 기록한다.
    """
    q = deque([(x, y)])
    visited[x][y] = 1  # 방문 체크 (기본값 1)

    while q:
        cx, cy = q.popleft()
        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m:
                # 이 로직을 통해서 주변이 바다라면 visited 값 증가 → 바다 개수 기록
                if graph[nx][ny] == 0:
                    visited[cx][cy] += 1
                # 이 로직을 통해서 연결된 빙산을 큐에 넣고 탐색 확장
                if visited[nx][ny] == 0 and graph[nx][ny] != 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1  # 방문 체크

while True:
    count = 0  # 빙산 덩어리 개수
    # 이 로직을 통해서 매년 visited 초기화 (방문 여부 + 바다 개수 기록 용도)
    visited = [[0] * m for _ in range(n)]

    # 1️⃣ 빙산 덩어리 탐색
    for i in range(n):
        for j in range(m):
            # 이 로직을 통해서 아직 방문하지 않은 빙산에서 BFS 시작
            if visited[i][j] == 0 and graph[i][j] > 0:
                bfs(i, j)
                count += 1  # 덩어리 하나 찾음

    # 2️⃣ 빙산 녹이기
    for i in range(n):
        for j in range(m):
            if visited[i][j] != 0:  # 빙산이었던 곳만 처리
                # visited[i][j]-1 = 주변 바다 개수
                graph[i][j] -= (visited[i][j] - 1)
                if graph[i][j] < 0:
                    graph[i][j] = 0

    # 3️⃣ 종료 조건 체크
    if count >= 2:
        print(time)
        break
    if count == 0:
        print(0)
        break

    time += 1  # 이 로직을 통해서 1년 증가