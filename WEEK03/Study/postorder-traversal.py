# 후위 순회 탐색 코드
def postorder(a):
    if a <= N:
        postorder(a*2)
        postorder(a*2 + 1)
        print(tree[a], end=' ')

N = 9
tree = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']
print(tree)
postorder(1)

#출력 H I D E B F G C A