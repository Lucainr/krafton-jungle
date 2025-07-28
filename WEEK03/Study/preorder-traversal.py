# 전위 순회 탐색 코드
def preorder(a):
    if a <= N:  # 현재 노드 번호 a가 트리 범위 안에 있을 때만 실행
        print(tree[a], end=' ')  # 1️⃣ 현재 노드를 먼저 출력 (전위 순회의 핵심)
        preorder(a*2)            # 2️⃣ 왼쪽 자식 노드 탐색 (a*2)
        preorder(a*2 + 1)        # 3️⃣ 오른쪽 자식 노드 탐색 (a*2+1)

N = 9
tree = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']
# index:  1    2    3    4    5    6    7    8    9
# value:  A    B    C    D    E    F    G    H    I
print(tree)
preorder(1)

