# 최소 스패닝 트리를 구하는 프로그램을 작성
# 최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치 합이 최소인 트리를 말한다.

# 첫째 줄에 정점의 개수 V와 간서의 개수 E가 주어짐
# 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다.
# 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미.
# C는 음수일 수 도 있으며, 절댓값이 1,000,000을 넘지 않는다.

# 출력 첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.

import sys
input = sys.stdin.readline

parent = {}

def make_set(x):
    parent[x] = x

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX == rootY:
        return False
    parent[rootY] = rootX
    return True

v, e = map(int, input().split())
edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

for i in range(1, v+1):
    make_set(i)

mst_weight = 0
cnt = 0

for a, b, c in edges:
    if union(a, b):
        mst_weight += c
        cnt += 1
        if cnt == v-1:  # MST는 V-1개의 간선에서 종료
            break

print(mst_weight)