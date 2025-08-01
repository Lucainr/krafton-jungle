def change_money():
    # 사용할 동전의 종류를 리스트로 정의
    # 일반적으로는 큰 단위부터 정렬되어 있지만, 여기서는 의도적으로 섞어둠
    coins = [100, 10, 500, 50]  

    # 거슬러 줘야 할 금액
    money = 1260                

    # 총 사용된 동전의 개수를 저장할 변수
    count = 0                   

    # 각 동전 단위별 사용 개수를 저장할 딕셔너리
    result_map = {}

    # 1. 선택 절차(Selection Procedure)
    # 가장 큰 단위의 동전부터 사용하기 위해 내림차순 정렬
    # reverse=True는 내림차순(큰 수부터 작은 수로) 정렬을 의미
    coins.sort(reverse=True)    # [500, 100, 50, 10]

    # 2. 적절성 검사(Feasibility Check)와 해답 계산
    for coin in coins:
        # 현재 단위의 동전이 몇 개 필요한지 계산
        # 예: 1260 // 500 = 2 (500원짜리 2개 필요)
        num = money // coin     

        # 현재 단위의 동전을 사용하고 남은 금액 계산
        # 예: 1260 % 500 = 260 (500원짜리 2개 사용 후 260원 남음)
        money %= coin           

        # 현재 동전의 사용 개수를 딕셔너리에 저장
        # str(coin)으로 키를 문자열로 변환
        result_map[str(coin)] = num

    # 3. 해답 검사(Solution Check)
    # 남은 금액이 0원이면 거스름돈이 정확히 계산된 것
    if money == 0:
        print("거스름돈 문제가 해결되었습니다.")

    # 각 동전별 사용 개수가 저장된 딕셔너리 반환
    return result_map


if __name__ == "__main__":
    # 함수 실행 및 결과 출력
    result = change_money()
    # 출력 예시: {'500': 2, '100': 2, '50': 1, '10': 1}
    # 500원 2개 + 100원 2개 + 50원 1개 + 10원 1개 = 1260원
    print(result)