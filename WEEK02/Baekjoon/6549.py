import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

n = arr[0]
histo = arr[1:]

print(n)
print(histo)