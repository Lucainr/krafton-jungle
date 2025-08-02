import sys

input = sys.stdin.readline
n, money = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

def change_money(money, coins):

    count = 0

    result_map = {}

    coins.sort(reverse=True)

    for coin in coins:
        num  = money // coin
        money %= coin
        count += num
        result_map[str(coin)] = num

    return count

result = change_money(money, coins)
print(result)