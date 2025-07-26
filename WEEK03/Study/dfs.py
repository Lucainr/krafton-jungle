MAX_VTXS = 256  # 최대 정점 개수

class AdjMatGraph:
    def __init__(self):
        self.size = 0  # 현재 정점 수
        self.vertices = []  # 정점 이름 저장
        self.adj = [[0] * MAX_VTXS for _ in range(MAX_VTXS)]  # 인접 행렬

    def insert_vertex(self, name):
        if self.size >= MAX_VTXS:
            print("Error: 정점 개수 초과")
            return
        self.vertices.append(name)
        self.size += 1

    def insert_edge(self, u, v):
        if u >= self.size or v >= self.size:
            print("Error: 잘못된 정점 번호")
            return
        self.adj[u][v] = 1
        self.adj[v][u] = 1  # 무방향 그래프라고 가정

    def is_linked(self, u, v):
        return self.adj[u][v] == 1

    def get_vertex(self, v):
        return self.vertices[v]

    def display(self):
        print(" ", end=" ")
        for i in range(self.size):
            print(self.vertices[i], end=" ")
        print()
        for i in range(self.size):
            print(self.vertices[i], end=" ")
            for j in range(self.size):
                print(self.adj[i][j], end=" ")
            print()

class SearchAdjMatGraph(AdjMatGraph):
    def __init__(self):
        super().__init__()
        self.visited = [False] * MAX_VTXS

    def reset_visited(self):
        for i in range(self.size):
            self.visited[i] = False

    def dfs(self, v):
        self.reset_visited()
        self.dfs_recur(v)

    def dfs_recur(self, v):
        self.visited[v] = True
        print(self.get_vertex(v), end=" ")

        for n in range(self.size):
            if self.is_linked(v, n) and not self.visited[n]:
                self.dfs_recur(n)

# 실행
if __name__ == "__main__":
    graph = SearchAdjMatGraph()

    # 정점 삽입
    for name in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        graph.insert_vertex(name)

    # 간선 삽입
    graph.insert_edge(0, 1)  # A-B
    graph.insert_edge(0, 2)  # A-C
    graph.insert_edge(1, 3)  # B-D
    graph.insert_edge(2, 3)  # C-D
    graph.insert_edge(2, 4)  # C-E
    graph.insert_edge(3, 5)  # D-F
    graph.insert_edge(4, 6)  # E-G
    graph.insert_edge(4, 7)  # E-H
    graph.insert_edge(6, 7)  # G-H

    print("== Display Graph ==")
    graph.display()

    print("- DFS => ", end="")
    graph.dfs(0)