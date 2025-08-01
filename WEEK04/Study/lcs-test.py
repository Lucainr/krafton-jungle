def lcs_length(str1, str2):
    # ① 문자열 길이
    len1 = len(str1)
    len2 = len(str2)

    # ② DP 테이블 초기화 (행: str2, 열: str1)
    # lcs[j][i] = str1의 앞 i글자와 str2의 앞 j글자까지의 LCS 길이
    lcs = [[0] * (len1 + 1) for _ in range(len2 + 1)]

    # ③ DP 테이블 채우기
    for i in range(1, len1 + 1):  # str1의 i번째 문자까지
        for j in range(1, len2 + 1):  # str2의 j번째 문자까지
            if str1[i - 1] == str2[j - 1]:  # ④ 문자가 같은 경우
                # 왼쪽 위 대각선 값 + 1
                lcs[j][i] = lcs[j - 1][i - 1] + 1
            else:  # ⑤ 문자가 다른 경우
                # 위쪽 값과 왼쪽 값 중 큰 값 선택
                lcs[j][i] = max(lcs[j - 1][i], lcs[j][i - 1])

    # ⑥ LCS 테이블 출력
    print("LCS 테이블:\n")
    for row in lcs:
        print(" ".join(map(str, row)))

    # ⑦ LCS 길이 출력
    print("\nLCS 길이:", lcs[len2][len1])


if __name__ == "__main__":
    str1 = "ACAYKP"
    str2 = "CAPCAK"
    lcs_length(str1, str2)
