import sys

n = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))

data.sort()

m = int(sys.stdin.readline())

check_data = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    if data.count(check_data[i]) == 1:
        print(1)
        
    else:
        print(0)