def knapsack_optimized(W, weights, values, n):
    dp = [0] * (W + 1)

    for i in range(n):
        for w in range(W, weights[i]-1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[W]

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5
print(knapsack_optimized(W, weights, values, len(weights)))  # 7