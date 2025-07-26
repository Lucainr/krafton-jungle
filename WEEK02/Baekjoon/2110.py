import sys

# 집 개수 N, 공유기 개수 C 입력
n, c = map(int, sys.stdin.readline().split())

# 집들의 좌표 입력받기
houses = [int(sys.stdin.readline()) for _ in range(n)]

# 집 위치 정렬 (가까운 순서로 정렬)
houses.sort()

# 특정 거리로 공유기 설치가 가능한지 확인하는 함수
def can_install(distance):
    count = 1  # 첫 번째 집에는 무조건 설치
    last_installed = houses[0]  # 마지막으로 설치한 위치 기록

    # 두 번째 집부터 확인
    for i in range(1, n):
        # 이전 공유기와의 거리가 distance 이상이면 설치 가능
        if houses[i] - last_installed >= distance:
            count += 1
            last_installed = houses[i]  # 새로 설치한 위치 갱신

    # C개 이상 설치할 수 있으면 True, 아니면 False
    return count >= c

# 이분 탐색 시작: 가능한 최소 거리와 최대 거리
left = 1  # 최소 거리
right = houses[-1] - houses[0]  # 최대 거리 (가장 멀리 떨어진 두 집 차이)
result = 0  # 정답 저장 변수

while left <= right:
    mid = (left + right) // 2  # 중간 거리 후보
    if can_install(mid):  # 이 거리로 공유기 설치가 가능하면
        result = mid      # 일단 저장
        left = mid + 1    # 더 먼 거리도 되는지 시도
    else:
        right = mid - 1   # 거리를 줄여서 다시 시도

# 결과 출력
print(result)