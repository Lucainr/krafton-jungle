from collections import deque  # deque(덱)을 사용하기 위해 collections 모듈에서 import
# 덱은 양쪽에서 빠른 삽입/삭제가 가능해 큐 구현에 적합함

# BFS(너비 우선 탐색) 메소드 정의
def bfs(graph, start, visited):
    queue = deque([start])  # 1️⃣ 시작 노드를 큐에 넣고 초기화
    visited[start] = True   # 2️⃣ 시작 노드를 방문 처리

    # 큐가 빌 때까지 반복 (탐색할 노드가 없을 때까지)
    while queue:
        v = queue.popleft()  # 3️⃣ 큐의 가장 왼쪽(앞쪽)에서 노드를 꺼냄 (FIFO)
        print(v, end='')     # 4️⃣ 현재 노드 출력 (탐색 순서 확인용)

        # 5️⃣ 현재 노드와 연결된 모든 인접 노드 확인
        for i in graph[v]:
            if not visited[i]:        # 6️⃣ 아직 방문하지 않은 노드라면
                queue.append(i)       # 7️⃣ 큐에 추가 (다음 탐색 대상으로 등록)
                visited[i] = True     # 8️⃣ 방문 처리 (중복 방문 방지)

# 그래프를 표현하는 인접 리스트(2차원 리스트)
graph = []

# 각 노드의 방문 여부를 표현하는 1차원 리스트 (False로 초기화 필요)
visited = []

# bfs 함수 호출: graph의 1번 노드부터 시작
bfs(graph, 1, visited)