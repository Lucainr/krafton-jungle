def lcs_length(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    # 2차원 리스트 초기화 (len2+1 x len1+1)
    lcs = [[0] * (len1 + 1) for _ in range(len2 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            # 비교하는 문자가 같은 경우 : 왼쪽 대각선 값 + 1
            if str1[i - 1] == str2[j - 1]:
                lcs[j][i] = lcs[j - 1][i - 1] + 1
            # 다른 경우 : 위, 왼쪽 중 큰 값
            else:
                lcs[j][i] = max(lcs[j - 1][i], lcs[j][i - 1])

    # LCS 테이블 출력
    print("LCS 테이블:\n")
    for row in lcs:
        print(" ".join(map(str, row)))

    print("\nLCS 길이:", lcs[len2][len1])


if __name__ == "__main__":
    str1 = "ACAYKP"
    str2 = "CAPCAK"
    lcs_length(str1, str2)