# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

# 전위 순회한 결과 : ABDCEFG // (루트)(왼쪽자식)(오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽자식)(루트)(오른쪽 자식)
# 후위 순회한 결과 : DBRGFCA // (왼쪽자식)(오른쪽 자식)(루트)

# 입력
# 첫째 줄 - 이진 트리의 노드 개수 N(1 <= N <= 26)이 주어짐
# 둘째 줄 - N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어짐.
# 노드의 이름은 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 됨
# 자식 노드가 없는 경우에는 .으로 표현

import sys

input = sys.stdin.readline

n = int(input())
tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)

# 전위 순회
def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1])

# 중위 순회
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])
# 후위 순회
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])    # 왼쪽 자식 순회
    postorder(tree[node][1])    # 오른쪽 자식 순회
    print(node, end='')         # 현재 노드 출력

print(tree)
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()