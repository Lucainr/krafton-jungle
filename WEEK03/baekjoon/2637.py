# 어떤 장난감을 여러가지 부품으로 조립하여 만들려고한다.
# 이 장난감을 만드는데는 기본 부품과 그 기본 부품으로 조립하여 만든 중간 부품이 사용된다.
# 기본 부품은 다른 부품을 사용하여 조립될 수 없는 부품이다.
# 중간 부품은 또 다른 중간 부품이나 기본 부품을 이용하여 만들어지는 부품이다.

# 첫째 줄에는 자연수 N , 1부터 N-1까지는 기본 부품이나 중간 부품의 번호를 나타내고, N은 완제품의 번호를 나타낸다.
# 다음 줄에는 자연수 M이 주어지고
# 그 다음 M개의 줄에는 어떤 부품을 완성하는데 필요한 부품들 간의 관계가 3개의 자연수 X, Y, K로 주어진다.
# 이 뜻은 "중간 부품이나 완제품 X를 만드는데 중간 부품 혹은 기본 부품 Y가 K개 필요하다"는 뜻이다.
# 두 중간 부품이 서로를 필요로 하는 경우가 없다.

# 하나의 오ㅘㄴ제품을 조립하는데 필요한 기본 부품의 수를 한 줄에 하나씩 출력하되(중간 부품은 출력하지 않음),
# 반드시 기본 부품의 번호가 작은 것부터 큰 순서가 되도록 한다. 각 줄에는 기본 부품의 번호와 소요 개수를 출력한다.

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
connect = [[] for _ in range(n + 1)]
needs = [[0] * (n + 1) for _ in range(n + 1)]
q = deque()
degree = [0] * (n + 1)

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    connect[b].append((a, c))
    degree[a] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for next, next_need in connect[now]:
        if needs[now].count(0) == n + 1:
            needs[next][now] += next_need
        else:
            for i in range(1, n + 1):
                needs[next][i] += needs[now][i] * next_need
        degree[next] -= 1
        if degree[next] == 0:
            q.append(next)

# ✅ index 1부터 출력 (0번 부품 제외)
for idx, val in enumerate(needs[n]):
    if idx > 0 and val > 0:
        print(idx, val)