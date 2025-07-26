# 초기화: 부모를 자기 자신으로
parent = {}

def make_set(x):
    parent[x] = x

# Find: 경로 압축 적용
def find(x):
    if x not in parent:
        return None
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# Union
def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX is None or rootY is None:
        return False
    if rootX != rootY:
        parent[rootY] = rootX
    return True

# 간선 정보 (가중치, 시작점, 끝점)
edges = [
    (1, 'A', 'B'),
    (3, 'A', 'C'),
    (2, 'B', 'C'),
    (4, 'B', 'D')
]

# 각 정점을 make_set
vertices = set()
for w, u, v in edges:
    vertices.add(u)
    vertices.add(v)

for vertex in vertices:
    make_set(vertex)

# 가중치 기준으로 간선 정렬
edges.sort()  # 가중치가 첫 번째 요소이므로 자동으로 가중치 기준 정렬

# Kruskal 알고리즘 수행
mst_weight = 0
mst_edges = []

for w, u, v in edges:
    if find(u) != find(v):
        if union(u, v):
            mst_weight += w
            mst_edges.append((u, v, w))
            print(f"간선 {u}-{v} (가중치: {w})가 MST에 추가됨")

print("MST 전체 가중치:", mst_weight)
print("MST 간선들:", mst_edges)