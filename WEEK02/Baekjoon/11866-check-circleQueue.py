import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

queue = deque(range(1, n + 1))
result = []

while queue:
    queue.rotate(-(k - 1))  # 왼쪽으로 k-1번 회전 (k번째가 맨 앞으로 오도록)
    result.append(queue.popleft())  # 맨 앞 요소 제거

print("<" + ", ".join(map(str, result)) + ">")