# 전위 순회 탐색 코드
def preorder(a):
    if a <= N:
        print(tree[a], end=' ')
        preorder(a*2)
        preorder(a*2 + 1)

N = 9
tree = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']
print(tree)
preorder(1)

