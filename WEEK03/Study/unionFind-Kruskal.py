# =========================
# 🔗 Union-Find (Disjoint Set)
# =========================

parent = {}

# ✅ 초기화: 각 노드의 부모를 자기 자신으로 설정
def make_set(x):
    parent[x] = x

# ✅ Find: 경로 압축(Path Compression)
def find(x):
    # x의 부모가 자기 자신이 아니면 루트를 찾아 올라가면서 부모 갱신
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# ✅ Union: 두 집합을 합침
def union(x, y):
    rootX = find(x)
    rootY = find(y)
    # 같은 루트라면 이미 연결된 상태 → 사이클 발생
    if rootX == rootY:
        return False
    # 임의의 규칙으로 rootY를 rootX 밑에 붙임
    parent[rootY] = rootX
    return True

# =========================
# 📌 Kruskal Algorithm
# =========================

# (가중치, 시작점, 끝점)
edges = [
    (1, 'A', 'B'),
    (3, 'A', 'C'),
    (2, 'B', 'C'),
    (4, 'B', 'D')
]

# ✅ 정점 목록 추출 후 make_set으로 초기화
vertices = set()
for w, u, v in edges:
    vertices.add(u)
    vertices.add(v)

for vertex in vertices:
    make_set(vertex)

# ✅ 간선들을 가중치 기준으로 정렬
edges.sort()

mst_weight = 0
mst_edges = []

# ✅ Kruskal 수행
for w, u, v in edges:
    # 두 정점이 같은 집합에 있지 않으면 MST에 추가
    if union(u, v):
        mst_weight += w
        mst_edges.append((u, v, w))
        print(f"✔ 간선 {u}-{v} (가중치 {w}) 추가됨")

# ✅ 결과 출력
print("\n📌 최소 신장 트리(MST) 결과")
print("총 가중치:", mst_weight)
print("선택된 간선들:", mst_edges)