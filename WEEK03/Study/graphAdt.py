class Graph:
    def __init__(self):
        self.vertices = []
        self.adj_matrix = []

    def add_vertex(self, v):
        if v in self.vertices:
            print(f"Vertex {v} already exists.")
            return
        self.vertices.append(v)
        # 기존 행에 0 추가
        for row in self.adj_matrix:
            row.append(0)
        # 새 행 추가
        self.adj_matrix.append([0] * len(self.vertices))

    def add_edge(self, u, v):
        if u not in self.vertices or v not in self.vertices:
            print("One or both vertices not found.")
            return
        i, j = self.vertices.index(u), self.vertices.index(v)
        self.adj_matrix[i][j] = 1  # 방향 그래프: u → v

    def remove_vertex(self, v):
        if v not in self.vertices:
            print(f"Vertex {v} not found.")
            return
        idx = self.vertices.index(v)
        self.vertices.pop(idx)
        self.adj_matrix.pop(idx)
        for row in self.adj_matrix:
            row.pop(idx)

    def remove_edge(self, u, v):
        if u not in self.vertices or v not in self.vertices:
            print("One or both vertices not found.")
            return
        i, j = self.vertices.index(u), self.vertices.index(v)
        self.adj_matrix[i][j] = 0

    def has_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            i, j = self.vertices.index(u), self.vertices.index(v)
            return self.adj_matrix[i][j] == 1
        return False

    def get_adjacent(self, v):
        if v not in self.vertices:
            print(f"Vertex {v} not found.")
            return []
        idx = self.vertices.index(v)
        return [self.vertices[i] for i, val in enumerate(self.adj_matrix[idx]) if val == 1]

    def display(self):
        print("   ", " ".join(self.vertices))
        for i, row in enumerate(self.adj_matrix):
            print(f"{self.vertices[i]}: ", " ".join(map(str, row)))


# 사용 예시
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")
g.display()

print("A → B?", g.has_edge("A", "B"))  # True
print("B의 인접 정점:", g.get_adjacent("B"))  # ['C']