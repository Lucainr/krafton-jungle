def knapsack_dp(W, weights, values, n):
    # dp[i][w] = i번째 아이템까지 고려했을 때, 용량 w에서의 최대 가치
    # 행: 아이템 수 (0~n), 열: 배낭 용량 (0~W)
    # 초기값: 모두 0 (아이템 0개이거나, 용량이 0이면 가치 = 0)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # i = 고려할 아이템의 개수 (1~n)
    for i in range(1, n + 1):
        # w = 현재 배낭 용량 (1~W)
        for w in range(1, W + 1):
            # 현재 아이템의 무게가 현재 용량 w보다 작거나 같으면 → 담을 수 있음
            if weights[i-1] <= w:
                # (1) 담는 경우 → 현재 아이템 가치 + 남은 용량(w - 아이템 무게)의 최대 가치
                include = values[i-1] + dp[i-1][w - weights[i-1]]
                # (2) 안 담는 경우 → 이전 아이템까지 고려한 현재 용량 w의 최대 가치
                exclude = dp[i-1][w]
                # 두 경우 중 더 큰 값을 선택
                dp[i][w] = max(include, exclude)
            else:
                # 현재 아이템이 너무 무거워서 담을 수 없으면 → 안 담는 경우의 값 그대로 유지
                dp[i][w] = dp[i-1][w]

    # dp[n][W] = 모든 아이템을 고려했을 때, 용량 W에서의 최대 가치
    return dp[n][W]


# 예제 데이터
weights = [2, 3, 4, 5]  # 각 아이템의 무게
values = [3, 4, 5, 6]   # 각 아이템의 가치
W = 5                   # 배낭의 최대 용량

# 최대 가치 출력 (결과: 7)
print(knapsack_dp(W, weights, values, len(weights)))  # 7