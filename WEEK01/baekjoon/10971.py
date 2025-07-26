import sys
from itertools import permutations

n = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_cost = float('inf')

for perm in permutations(range(1, n)):
    cost = 0
    valid = True
    current_route = (0,) + perm

    for i in range(n - 1):
        if W[current_route[i]][current_route[i + 1]] == 0:
            valid = False
            break
        else:
            cost += W[current_route[i]][current_route[i + 1]]
        if cost >= min_cost:
            valid = False
            break

    if valid and W[current_route[-1]][current_route[0]] != 0:
        cost += W[current_route[-1]][current_route[0]]
        min_cost = min(min_cost, cost)

print(min_cost)

# import sys
# from itertools import permutations

# n = int(sys.stdin.readline())
# W = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# min_cost = float('inf')

# for perm in permutations(range(n)):
#     cost=0
#     valid = True
#     for i in range(n-1):
#         if W[perm[i]][perm[i+1]] == 0:
#             valid = False
#             break
#         else:
#             cost += W[perm[i]][perm[i+1]]
            
#     if valid and W[perm[-1]][perm[0]] != 0:
#         cost += W[perm[-1]][perm[0]]
#         min_cost = min(min_cost, cost)
        
# print(min_cost)