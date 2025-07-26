import sys

n = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))
stack = []
answer_index = [0] * n

for i in range(n):
    while stack and tops[stack[-1]] < tops[i]:
        stack.pop()

    if stack:
        answer_index[i] = stack[-1] + 1  # 인덱스를 번호로 바꾸기 위해 +1

    stack.append(i)

print(' '.join(map(str, answer_index)))