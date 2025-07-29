# DFS(깊이 우선 탐색) 메소드 정의
def dfs(graph, v, visited):
    visited[v] = True       # 1️⃣ 현재 노드를 방문 처리
    print(v, end='')        # 2️⃣ 현재 노드 출력 (탐색 순서 확인용)

    # 3️⃣ 현재 노드(v)에 연결된 모든 인접 노드(i) 탐색
    for i in graph[v]:
        if not visited[i]:  # 4️⃣ 아직 방문하지 않은 노드라면
            dfs(graph, i, visited)  # 5️⃣ 재귀 호출로 깊이 탐색 진행

# 그래프를 표현하는 인접 리스트(2차원 리스트)
graph = []

# 각 노드의 방문 여부를 표현하는 1차원 리스트 (False로 초기화 필요)
visited = []

# dfs 함수 호출: graph의 1번 노드부터 시작
dfs(graph, 1, visited)

