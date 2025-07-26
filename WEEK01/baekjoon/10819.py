from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

max_value = 0

for perm in permutations(arr):
    temp = 0
    for i in range(n - 1):
        temp += abs(perm[i] - perm[i+1])
    if temp > max_value:
        max_value = temp

print(max_value)