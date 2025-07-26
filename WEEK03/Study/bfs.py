from collections import deque

MAX_VTXS = 256

# 인접 리스트의 노드 구조
class Node:
    def __init__(self, vid, link=None):
        self.id = vid
        self.link = link

class AdjListGraph:
    def __init__(self):
        self.size = 0
        self.vertices = []  # 정점 이름
        self.adjList = [None] * MAX_VTXS  # 각 정점에 대한 인접 리스트 시작점

    def insert_vertex(self, name):
        if self.size >= MAX_VTXS:
            print("Error: 정점 수 초과")
            return
        self.vertices.append(name)
        self.size += 1

    def insert_edge(self, u, v):
        if u >= self.size or v >= self.size:
            print("Error: 잘못된 정점 번호")
            return
        # 양방향 그래프 (무방향)
        self.adjList[u] = Node(v, self.adjList[u])
        self.adjList[v] = Node(u, self.adjList[v])

    def get_vertex(self, v):
        return self.vertices[v]

    def display(self):
        for i in range(self.size):
            print(f"{self.get_vertex(i)}:", end=" ")
            node = self.adjList[i]
            while node:
                print(f"{self.get_vertex(node.id)}", end=" -> ")
                node = node.link
            print("None")

class SearchAdjListGraph(AdjListGraph):
    def __init__(self):
        super().__init__()
        self.visited = [False] * MAX_VTXS

    def reset_visited(self):
        for i in range(self.size):
            self.visited[i] = False

    def bfs(self, v):
        self.reset_visited()

        self.visited[v] = True
        print(self.get_vertex(v), end=" ")

        queue = deque()
        queue.append(v)

        while queue:
            v = queue.popleft()
            node = self.adjList[v]

            while node:
                nid = node.id
                if not self.visited[nid]:
                    print(self.get_vertex(nid), end=" ")
                    self.visited[nid] = True
                    queue.append(nid)
                node = node.link

# 실행 부분
if __name__ == "__main__":
    graph = SearchAdjListGraph()

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

    print("- BFS => ", end="")
    graph.bfs(0)