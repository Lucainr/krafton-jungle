# 중위 순회 탐색 코드
def inorder(a):
    if a <= N:
        inorder(a*2)
        print(tree[a], end=' ')
        inorder(a*2 + 1)

N = 9
tree = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']
print(tree)
inorder(1)

#출력 H D I B E A F C G
