# 피보나치 (Bottom-Up)
n = 10
dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])  # 55