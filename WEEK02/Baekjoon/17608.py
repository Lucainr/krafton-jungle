import sys

stack = []

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    stack.append(num)

cnt = 1
h = stack.pop()

while stack:
    current = stack.pop()
    if current > h:
        cnt += 1
        h = current
print(cnt)