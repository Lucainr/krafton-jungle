def knapsack_recursive(W, weights, values, n):
    if n == 0 or W == 0:
        return 0
    if weights[n-1] > W:
        return knapsack_recursive(W, weights, values, n-1)
    else:
        return max(
            values[n-1] + knapsack_recursive(W - weights[n-1], weights, values, n-1),
            knapsack_recursive(W, weights, values, n-1)
        )

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5
print(knapsack_recursive(W, weights, values, len(weights)))  # 7