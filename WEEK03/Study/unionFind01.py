# 초기화: 부모를 자기 자신으로
parent = {}

def make_set(x):
    parent[x] = x

# Find: 경로 압축 적용
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# Union
def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parent[rootY] = rootX  # 또는 parent[rootX] = rootY 도 가능

# 집합 초기화
for x in ['a', 'b', 'c', 'd', 'e']:
    make_set(x)

union('a', 'b')
union('b', 'c')

print(find('a'))  # → 'a'
print(find('c'))  # → 'a' (경로 압축됨)

union('d', 'e')

print(find('d'))  # → 'd'
print(find('e'))  # → 'd'

union('c', 'e')  # 모든 원소가 같은 집합이 됨

print(find('e'))  # → 'a'