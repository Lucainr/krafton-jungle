# N명의 학생들을 키 순서대로 줄을 세우려고 한다.
# 각 학생의 키를 직접 재서 정렬하면 간단하겠지만, 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용.
# 일부 학생들의 키만을 비교해 보았다.

# 첫째 줄에 N이 주어진다. M은 키를 비교한 횟수이다.
# 다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다.
# 이는 학생 A가 학생 B의 앞에 서야 한다는 의미이다.

# 첫째 줄에 학생들을 앞에서부터 줄을 세운 결과를 출력한다.
# 답이 여러 가지인 경우에는 아무거나 출력한다.

import sys
from collections import deque

def topological_sort(n, edges):
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) == n:
        return print(' '.join(map(str, result)))
    else:
        return []

n, m = map(int, sys.stdin.readline().split())
edges = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edges.append((a, b))

topological_sort(n, edges)