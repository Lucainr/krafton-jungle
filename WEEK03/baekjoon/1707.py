# 그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 이분 그래프(Bipartite Graph)라 부른다.
# 그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

# 첫째 줄에 테스트 케이스의 개수 k 가 주어짐
# 각 테스트 케이스의 첫째 줄에는 그래프의 정점 개수 V와 간선의 개수 E가 빈칸을 사이에 두고 순서대로 주어진다.
# 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다.
# 이어서 둘째 줄 부터 E개의 줄에 걸쳐 간선ㅇ네 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호 u, v가 빈칸을 사이에 두고 주어진다.

# k개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    color = [0] * V

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    def dfs(node, c):
        color[node] = c
        for nxt in graph[node]:
            if color[nxt] == 0:
                if not dfs(nxt, -c):
                    return False
            elif color[nxt] == c:
                return False
        return True

    result = True
    for i in range(V):
        if color[i] == 0:
            if not dfs(i, 1):
                result = False
                break

    print("YES" if result else "NO")
