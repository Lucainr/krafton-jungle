import sys

n = int(sys.stdin.readline())
count = [0] * 10001  # 숫자 값 범위가 1 ~ 10,000

for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(1, 10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)