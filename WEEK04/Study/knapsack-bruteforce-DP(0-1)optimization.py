def knapsack_dp(W, weights, values, n):
    # dp[i][w] = i번째 아이템까지 고려했을 때, 용량 w에서의 최대 가치
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # i = 아이템 인덱스 (1 ~ n)
    for i in range(1, n + 1):
        # w = 현재 배낭 용량 (1 ~ W)
        for w in range(1, W + 1):
            if weights[i-1] <= w:
                # (1) 현재 아이템 담는 경우
                include = values[i-1] + dp[i-1][w - weights[i-1]]
                # (2) 현재 아이템 안 담는 경우
                exclude = dp[i-1][w]
                # 더 큰 값 선택
                dp[i][w] = max(include, exclude)
            else:
                # 현재 아이템이 너무 무거워서 못 담음 → 이전 값 그대로
                dp[i][w] = dp[i-1][w]

    # 최종 결과: 모든 아이템 고려 & 용량 W일 때의 최대 가치
    return dp[n][W]

# 예제 데이터
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5
print(knapsack_dp(W, weights, values, len(weights)))  # 7