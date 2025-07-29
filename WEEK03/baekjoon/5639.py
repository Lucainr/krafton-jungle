import sys
# 재귀 제한을 늘려줍니다 (이진 검색 트리의 노드 수가 많을 수 있으므로)
sys.setrecursionlimit(10**9)

# 입력받은 전위 순회 결과를 저장할 리스트
nums = []

# 입력이 끝날 때까지 노드의 값들을 입력받음
while True:
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break

def postorder(s, e):
    """
    전위 순회 결과를 이용해 후위 순회 결과를 출력하는 함수
    s: 현재 부분 트리의 시작 인덱스
    e: 현재 부분 트리의 끝 인덱스
    """
    # 시작 인덱스가 끝 인덱스보다 크면 유효하지 않은 범위이므로 종료
    if s > e:
        return

    # mid는 오른쪽 서브트리의 시작점을 나타냄
    # 초기값을 e + 1로 설정 (오른쪽 서브트리가 없는 경우를 대비)
    mid = e + 1

    # 현재 루트 노드보다 큰 값을 찾아 
    # 왼쪽 서브트리와 오른쪽 서브트리를 구분
    for i in range(s+1, e+1):
        if nums[s] < nums[i]:    # 루트보다 큰 값을 찾으면
            mid = i              # 이 지점이 오른쪽 서브트리의 시작점
            break

    # 후위 순회 실행
    # 1. 왼쪽 서브트리 순회 (s+1 ~ mid-1)
    postorder(s+1, mid-1)
    # 2. 오른쪽 서브트리 순회 (mid ~ e)
    postorder(mid, e)
    # 3. 현재 노드 출력
    print(nums[s])

# 전체 트리에 대해 후위 순회 실행
postorder(0, len(nums)-1)