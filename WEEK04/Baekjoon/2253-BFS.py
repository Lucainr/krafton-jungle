import sys
from collections import deque

# N: 마지막 돌 번호 (목표 지점)
# M: 작은 돌의 개수
N, M = map(int, sys.stdin.readline().split())

# check[i]: i번 돌에 도착했을 때 사용한 점프 거리를 저장
#   → 같은 돌에 같은 점프 거리로 도착하는 경우는 중복 탐색을 방지
check = [[] for _ in range(N + 1)]

# 작은 돌의 위치를 저장하는 집합 (빠른 조회를 위해 set 사용)
small_rock = set()
for _ in range(M):
    small = int(sys.stdin.readline())
    small_rock.add(small)

def solution(N, check, small_rock):
    # BFS 큐 초기화: (현재 위치, 이전 점프 거리, 현재까지의 점프 횟수)
    # 시작은 1번 돌, 이전 점프 거리 0, 점프 횟수 0
    queue = deque([(1, 0, 0)])

    # BFS 탐색 시작
    while queue:
        location, jump, n = queue.popleft()  # 현재 위치, 이전 점프, 점프 횟수 꺼냄

        # 다음 점프 거리 후보: 이전 점프 +1, 동일, -1
        for x in [jump + 1, jump, jump - 1]:
            if x > 0:  # 점프 거리는 양수여야 함
                next_location = location + x  # 다음 위치 계산

                # 다음 위치가 목표 지점이면 점프 횟수 + 1 반환
                if next_location == N:
                    return n + 1

                # 다음 위치가 범위 내이고, 작은 돌이 아니며,
                # 같은 점프 거리로 도착한 적이 없는 경우
                if (next_location < N and
                        next_location not in small_rock and
                        x not in check[next_location]):

                    # 해당 위치에 점프 거리 기록
                    check[next_location].append(x)
                    # 큐에 다음 상태 추가 (다음 위치, 점프 거리, 점프 횟수 + 1)
                    queue.append((next_location, x, n + 1))

    # 도착할 수 없는 경우 -1 반환
    return -1

# 결과 출력
print(solution(N, check, small_rock))