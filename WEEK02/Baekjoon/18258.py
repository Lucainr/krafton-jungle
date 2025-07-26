from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

queue = deque()

for _ in range(n):
    cmd = sys.stdin.readline().strip()
    
    if cmd.startswith("push"):
        _, num = cmd.split()
        queue.append(num)
    elif cmd == "pop":
        print(queue.popleft() if queue else -1)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        print(0 if queue else 1)
    elif cmd == "front":
        print(queue[0] if queue else -1)
    elif cmd == "back":
        print(queue[-1] if queue else -1)