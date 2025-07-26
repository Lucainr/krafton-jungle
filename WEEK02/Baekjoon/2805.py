import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
result = 0

while start <= end:
    mid = (start + end) // 2  # 현재 절단기 높이
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid  # 잘린 나무 길이 합산

    if total >= m:
        result = mid  # 일단 저장하고
        start = mid + 1  # 더 높게 해도 되는지 확인
    else:
        end = mid - 1

print(result)