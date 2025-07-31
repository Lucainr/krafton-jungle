def change_money():
    coins = [100, 10, 500, 50]  # 동전 종류
    money = 1260                # 거스름돈
    count = 0                   # 동전 사용 개수
    result_map = {}

    # 1. 선택 절차: 가치가 큰 동전부터 선택
    coins.sort(reverse=True)

    # 2. 적절성 검사 + 계산
    for coin in coins:
        num = money // coin     # 해당 동전 개수
        money %= coin           # 남은 금액
        result_map[str(coin)] = num

    # 3. 해답 검사
    if money == 0:
        print("거스름돈 문제가 해결되었습니다.")

    # 결과 반환
    return result_map


if __name__ == "__main__":
    result = change_money()
    print(result)  # 예: {'500': 2, '100': 2, '50': 1, '10': 1}