def knapsack_recursive(W, weights, values, n):
    # 1️⃣ 종료 조건: 아이템이 없거나(W=0) 배낭 용량이 0이면 가치 0
    if n == 0 or W == 0:
        return 0

    # 2️⃣ 현재 아이템 무게가 배낭 용량보다 크면 → 담을 수 없음 → 이전 아이템만 고려
    if weights[n-1] > W:
        return knapsack_recursive(W, weights, values, n-1)

    else:
        # 3️⃣ 두 가지 경우 중 큰 값 선택
        #   (1) 현재 아이템을 담는 경우 → 가치 + 남은 용량에 대한 결과
        #   (2) 현재 아이템을 담지 않는 경우
        return max(
            values[n-1] + knapsack_recursive(W - weights[n-1], weights, values, n-1),
            knapsack_recursive(W, weights, values, n-1)
        )

# 예제 데이터
weights = [2, 3, 4, 5]   # 각 아이템의 무게
values = [3, 4, 5, 6]    # 각 아이템의 가치
W = 5                    # 배낭 최대 용량

# 결과 출력 (최대 가치)
print(knapsack_recursive(W, weights, values, len(weights)))  # 7