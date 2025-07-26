count = int(input())
count_list = list(map(int, input().split()))

ans = 0

for num in count_list:
    if num < 2:
        continue  # 1은 소수가 아니니까 pass
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        ans += 1

print(ans)