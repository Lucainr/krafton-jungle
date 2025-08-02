import sys

input = sys.stdin.readline

n, k = map(int, input().split())    # n: 물품의 수, k: 버틸 수 있는 무게
dp = [[0] * (k + 1) for _ in range(n + 1)]    # 2차원 DP 테이블 생성

weights = [0]
values = [0]

# 물품 정보 입력 받기
for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

# 냅색 알고리즘 실행
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if weights[i] <= j:    # 현재 물품을 배낭에 넣을 수 있는 경우
            dp[i][j] = max(values[i] + dp[i-1][j-weights[i]], dp[i-1][j])
        else:    # 현재 물품을 배낭에 넣을 수 없는 경우
            dp[i][j] = dp[i-1][j]

print(dp[n][k])