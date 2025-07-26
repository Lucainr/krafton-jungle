import sys

input = sys.stdin.readline  # 입력 속도 향상을 위해 input 재정의

# 수열 A의 크기 입력
n = int(input())

# 수열 A 입력 및 정수 리스트로 변환
data = list(map(int, input().split()))

# 이분 탐색을 위해 오름차순 정렬 (필수)
data.sort()

# 수열 B의 크기 입력
m = int(input())

# 수열 B 입력 및 정수 리스트로 변환
check_data = list(map(int, input().split()))

# 이분 탐색 함수 정의
def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # 왼쪽 인덱스와 오른쪽 인덱스 초기화

    # 탐색 구간이 존재하는 동안 반복
    while left <= right:
        mid = (left + right) // 2  # 중간 인덱스 계산
        if arr[mid] == target:     # 중간값이 찾고자 하는 값이면
            return True            # True 반환 (값 존재)
        elif arr[mid] < target:    # 중간값보다 target이 크면
            left = mid + 1         # 오른쪽 절반으로 범위 이동
        else:                      # 중간값보다 target이 작으면
            right = mid - 1        # 왼쪽 절반으로 범위 이동

    return False  # 끝까지 못 찾으면 False 반환

# 수열 B에 있는 각 값에 대해 A에서 존재 여부 확인
for num in check_data:
    if binary_search(data, num):  # 이분 탐색 결과가 True이면
        print(1)  # 존재하므로 1 출력
    else:
        print(0)  # 존재하지 않으므로 0 출력