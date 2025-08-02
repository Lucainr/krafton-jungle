import sys
input = sys.stdin.readline
INF = float('inf')
def solve():
    N, M = map(int, input().split())

    # 작은 돌 집합 생성
    small_stones = set()
    for _ in range(M):
        small_stones.add(int(input()))
    
    # dp[stone][speed]: stone번 돌에 speed로 도달하기 위한 최소 점프 횟수
    # 최대 speed는 약 sqrt(2N)보다 작음
    MAX_SPEED = int((2 * N) ** 0.5) + 1
    dp = [INF * (MAX_SPEED + 1) for _ in range(N + 1)]
    
    # 초기 상태: 첫 번째 돌에서 시작, 속도 0
    dp[1][0] = 0
    
    # 각 돌에 대해
    for stone in range(1, N):
        # 각 속도에 대해
        for speed in range(MAX_SPEED):
            # 현재 상태가 도달 가능하지 않으면 스킵
            if dp[stone][speed] == INF:
                continue
                
            # 가능한 다음 속도들에 대해 (-1, 0, +1)
            for next_speed in [speed-1, speed, speed+1]:
                # 속도가 유효한지 확인
                if next_speed <= 0 or next_speed >= MAX_SPEED:
                    continue
                    
                # 다음 돌 위치 계산
                next_stone = stone + next_speed
                
                # 범위를 벗어나거나 작은 돌이면 스킵
                if next_stone > N or next_stone in small_stones:
                    continue
                    
                # 최소 점프 횟수 갱신
                dp[next_stone][next_speed] = min(
                    dp[next_stone][next_speed],
                    dp[stone][speed] + 1
                )
    
    # N번 돌에 도달하는 최소 점프 횟수 찾기
    result = min(dp[N])
    
    # 도달할 수 없으면 -1 반환
    return result if result != INF else -1

print(solve())