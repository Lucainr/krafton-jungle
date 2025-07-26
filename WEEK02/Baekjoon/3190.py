import sys
from collections import deque
input = sys.stdin.readline
n = int(input()) # 보드 크기
k = int(input()) # 사과 개수
maps = [[0] * (n+1) for _ in range(n+1)]
for _ in range(k):# 사과의 위치
    x,y = map(int,input().split())
    maps[x][y] = 2 # 사과가 위치한 좌표에는 2로 표현
    
info = {} # dictionary (key : value)

l = int(input())
for _ in range(l):# 뱀의 방향변환정보 (초, 방향 L:왼쪽 D:오른쪽)
    sec, direct = input().split()
    info[int(sec)] = direct
time = 0

# ex) index +1로 보면 우에서 90 도 회전하면 하로 가는것
dx = [1,0,-1,0] # 방향 전환용 리스트 [우, 하, 좌, 상]
dy = [0,1,0,-1] # 방향 전환용 리스트 [우, 하, 좌, 상]

# 오른쪽으로 간다는 것은 x, y축을 기준으로 x 축으로 1칸씩 가는 것임, y축은 이동하지 X
# 아래(하)로 간다는 것은 x, y축을 기준으로 y 축으로 1칸씩 가는 것임, x축은 이동하지 X
# 왼쪽으로 간다는 것은 x, y축을 기준으로 x 축으로 -1칸씩 가는 것임, y축은 이동하지 X
# 위(상)로 간다는 것은 x, y축을 기준으로 y 축으로 -1칸씩 가는 것임. x축은 이동하지 X

x, y = 1, 1 # 뱀위 시작 위치는 (1, 1), 현재 방향은 오른쪽(d = 0)
maps[y][x] = 1 # -> 뱀을 표시. 0은 비어있는곳 1은 뱀의 위치, 2는 사과의 위치 표시
d = 0 # 뱡향 전환 index
snakes = deque([(1, 1)]) # 뱀의 몸통을 구성하는 좌표들을 저장 (머리부터 꼬리 순서)

while True: # Fxcking Simulation 시작
    
    # 다음 위치 계산 nx(next x), ny(next y)
    nx, ny = x+dx[d], y+dy[d] # x, y는 뱀이 현재 위치하고 있는 위치니 dx, dy의 방향 전환용 리스트를 통해 다음 위치를 계산
    # 따라서 nx, ny는 뱀의 다음 이동 좌표
    # ex) d = 0 이면 오른쪽이니, dx[0] = 1, dy=[0] = 0 이니까 (x+1, y)로 이동.
    
    # 뱀의 몸통에 닿거나 벽에 부딪히는 경우 종료
    if nx<=0 or ny<=0 or nx>n or ny>n or (nx,ny) in snakes:
        # nx 또는 ny가 보드 범위를 벗어 났다는 것은 벽에 충돌 했다는 뜻으로 종료 조건에 포함됨.
        # 또는 (nx, ny)가 snakes 안에 있다는 것은 자기 몸과 충돌했다는 뜻으로 게임 종료.
        break
    
    # 사과를 먹지 못하면 꼬리 없애기
    if maps[ny][nx]!=2: # 이동한 위치에 사과가 없는 경우를 처리
        # maps[ny][nx] == 2이면 사과가 있는 칸이고 아니면 빈칸 또는 자기 몸임.
        # 즉 사과를 안 먹은 경우 꼬리를 제거해야 뱀의 길이를 유지할 수 있음.
        
        # snakes는 뱀의 몸통을 머리 ~ 꼬리 순으로 저장한 deque구조.
        a,b = snakes.popleft() # 맨앞 (꼬리 위치)을 제거.
        maps[b][a]=0 # 보드에서도 꼬리 위치를 0으로 만들어 빈칸으로 처리
        
    x, y = nx, ny # 뱀의 머리를 다음 위치로 이동시킴.
    maps[y][x] = 1 # 새로운 머리 위치를 보드에 표시 (뱀 몸통)
    snakes.append((nx, ny)) # 다시 snakes라는 deque에 머리 위치를 추가해줌 (머리 방향으로 뱀이 늘어남)
    time+=1 # 1초 지잤으니 time 증가
	
    # 시간에 해당하는 방향전환 정보가 있을 경우
    if time in info.keys():
        if info[time] == "D": # "D"는 시계 방향으로 회전(오른쪽 90도 회전)
            d = (d+1)%4 # 0 ~ 3 까지 순환되도록 (d + 1) % 4 사용
        else: # "L"은 반시계 뱡향으로 회전 (왼쪽으로 90도 회전)
            nd = 3 if d==0 else d-1 # d-1을 하면 되지만, d==0 일때는 음수가 되므로 3으로 바꿔줌.
            d = nd # 방향 인덱스를 하나 감소시키되, 0일 경우 3으로 되돌림.

print(time+1) # 마지막으로 충돌이 일어난 시점이므로 +1 해줘야 실제 소요 시간임.