import sys

def hanoi(cnt : int, x : int, y : int):
    if cnt > 1:
        hanoi(cnt-1, x, 6-x-y)
        
    print(f'{x} {y}')
    
    if cnt > 1:
        hanoi(cnt-1, 6-x-y, y)
    
n = int(sys.stdin.readline())
print(2**n -1)

if n <= 20:
    hanoi(n, 1, 3)
  