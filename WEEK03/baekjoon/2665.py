# n * n 바둑판 모양 총 n^2개의 방이 있다.
# 일부분은 검은 방이고 나머지는 모두 휜 방이다.
# 검은 방은 사면이 벽으로 싸여있어 들어갈 수 없다.
# 서로 붙어 있는 두 개의 흰 방 사이에는 문이 있어서 지나다닐 수 있다.
# 윗줄 맨 왼쪽 방은 시작방으로서 항상 휜 방.
# 아랫줄 맨 오른쪽 방은 끝방으로서 역시 흰 방.

# 시작방에서 출발하여 길을 찾아 끝방으로 가는 것이 목적인데, 아래 그림의 경우에는 시작방에서 끝 방으로 갈 수가 없다.
# 그래서 부득이 검은 방 몇개를 휜 방으로 바꾸어야 하는데 되도록 적은 수의 방의 색을 바꾸고 싶다.

# 검은 방에서 흰 방으로 바꾸어야 할 최소의 수를 구하는 프로그램을 작성하시오.
# 검은 방을 하나도 휜방으로 바꾸지 않아도 되는경우는 0이 답이다.

# 첫 줄에는 한 줄에 들어가는 방의 수 n 이 주어지고
# 다음 n개의 줄의 각 줄 마다 0과 1이 이루어진 길이가 n인 수열이 주어진다.
# 0은 검은 방, 1은 휜 방을 나타낸다.

# 첫 줄에 휜 방으로 바꾸어야 할 최소의 검은 방의 수를 출력한다.

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 0
    
    while queue:
        x, y = queue.popleft()
        
        if x == n-1 and y == n-1:
            return visited[x][y]
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if arr[nx][ny] == '1':
                    queue.appendleft((nx, ny))  # 흰 방은 가중치 0
                    visited[nx][ny] = visited[x][y]
                else:
                    queue.append((nx, ny))      # 검은 방은 가중치 1
                    visited[nx][ny] = visited[x][y] + 1
                    
print(bfs())