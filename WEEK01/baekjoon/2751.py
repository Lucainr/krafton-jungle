import sys

cnt = int(sys.stdin.readline())
num_list = []

for _ in range(cnt):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

for i in num_list:
    print(i)