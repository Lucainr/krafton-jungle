# 8×8 종이
# → 4등분해서 4개의 4×4
# → 각 4×4가 한 색인지 확인
# → 아니라면 다시 4등분... 반복

import sys
input = sys.stdin.readline  # 빠른 입력을 위해 사용

# 전체 종이의 크기 N 입력
n = int(input())

# N×N 크기의 종이 정보 입력 (2차원 리스트)
# 0은 흰색, 1은 파란색
paper = [list(map(int, input().split())) for _ in range(n)]

# 흰색, 파란색 색종이 개수를 저장할 변수
white = 0
blue = 0

# 종이를 분할하고 색종이를 세는 재귀 함수
def divide(x, y, size):
    """
    (x, y): 현재 영역의 왼쪽 위 좌표
    size: 현재 영역의 한 변의 길이
    """
    global white, blue

    # 현재 영역의 첫 번째 칸 색상
    color = paper[x][y]

    # 해당 영역이 모두 같은 색인지 검사
    for i in range(x, x + size):
        for j in range(y, y + size):
            # 다른 색이 하나라도 있다면
            if paper[i][j] != color:
                # 4등분하여 재귀적으로 나눔
                half = size // 2
                divide(x, y, half)  # 왼쪽 위
                divide(x, y + half, half)  # 오른쪽 위
                divide(x + half, y, half)  # 왼쪽 아래
                divide(x + half, y + half, half)  # 오른쪽 아래
                return  # 더 이상 아래 코드를 실행하지 않고 종료

    # 모든 칸이 같은 색이면 색종이 수를 1 증가
    if color == 0:
        white += 1  # 흰색 색종이
    else:
        blue += 1   # 파란색 색종이

# 전체 종이에 대해 처음부터 분할 시작
divide(0, 0, n)

# 결과 출력
print(white)
print(blue)