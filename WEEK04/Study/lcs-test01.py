# LCS 문자열 복원

def lcs_with_string(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    # 2차원 리스트 초기화 (길이 저장용)
    lcs = [[0] * (len1 + 1) for _ in range(len2 + 1)]

    # LCS 테이블 채우기
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs[j][i] = lcs[j - 1][i - 1] + 1
            else:
                lcs[j][i] = max(lcs[j - 1][i], lcs[j][i - 1])

    # LCS 문자열 복원
    i, j = len1, len2
    lcs_str = []

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:  # 같은 문자면 LCS에 포함
            lcs_str.append(str1[i - 1])
            i -= 1
            j -= 1
        elif lcs[j - 1][i] > lcs[j][i - 1]:  # 위쪽 값이 더 크면 위로 이동
            j -= 1
        else:  # 왼쪽 값이 더 크면 왼쪽으로 이동
            i -= 1

    lcs_str.reverse()  # 거꾸로 저장했으니 뒤집기

    # LCS 테이블 출력
    print("LCS 테이블:\n")
    for row in lcs:
        print(" ".join(map(str, row)))

    print("\nLCS 길이:", lcs[len2][len1])
    print("LCS 문자열:", "".join(lcs_str))


if __name__ == "__main__":
    str1 = "ACAYKP"
    str2 = "CAPCAK"
    lcs_with_string(str1, str2)