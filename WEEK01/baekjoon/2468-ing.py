import sys

n = int(sys.stdin.readline())
H = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max_val = max(map(max, H))
min_val = min(map(min, H))
max_sur = 0

for num in range(min_val, max_val +1):
    cur_sur = 0
    for i in range(n):
        for j in range(len(H)):
            if num == H[i][j]:
                cur_sur += 1 

    print(f'{num}미터 안전지대 {cur_sur}')

    if cur_sur < max_sur:
        cur_sur = 0
    else:
        max_sur = cur_sur
        
print(max_sur)