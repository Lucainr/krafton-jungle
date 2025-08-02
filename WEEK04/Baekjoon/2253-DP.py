import sys

# N: 마지막 돌 번호 (목표)
# M: 작은 돌의 개수
N, M = map(int, sys.stdin.readline().split())

# dp[i][j] = i번 돌에 '점프 거리 j'로 도착했을 때의 최소 점프 횟수
# 점프 거리는 최대 int(sqrt(2*N)) + 1 까지만 고려 (물리적으로 가능한 최대 점프 거리)
dp = [[float('inf')] * (int((2 * N)**0.5) + 2) for _ in range(N + 1)]

# 시작점: 1번 돌에서 점프 거리 0으로 시작 → 점프 횟수 0
dp[1][0] = 0

# 작은 돌 위치 저장 (해당 위치는 점프 불가)
stone_set = set()
for _ in range(M):
    stone_set.add(int(sys.stdin.readline()))

# 2번 돌부터 N번 돌까지 DP 채우기
for i in range(2, N + 1):
    # 작은 돌이면 건너뛰기
    if i in stone_set:
        continue

    # 가능한 점프 거리 j 범위 설정
    # 최대 점프 거리는 현재 돌 번호 i에 대해 int(sqrt(2*i)) + 1
    for j in range(1, int((2 * i) ** 0.5) + 1):
        # i번 돌에 점프 거리 j로 도착하기 위해
        # 이전에 올 수 있는 경우는 (i - j)번 돌에서
        # 점프 거리 (j - 1), j, (j + 1) 중 하나였음
        dp[i][j] = min(
            dp[i - j][j - 1],  # 이전 점프 거리보다 1 작게
            dp[i - j][j],      # 이전 점프 거리와 같게
            dp[i - j][j + 1]   # 이전 점프 거리보다 1 크게
        ) + 1  # 점프 횟수 1 추가

# 결과 출력
# N번 돌에 도착한 최소 점프 횟수가 무한대이면 (-1) 출력
if min(dp[N]) == float('inf'):
    print(-1)
else:
    print(min(dp[N]))