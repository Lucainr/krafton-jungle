# 노드 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 링크드 리스트 클래스 정의
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next # current.next가 존재하지 않을 때 까지 next를 한다.
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


# 링크드 리스트 객체 생성 및 데이터 추가
linked_list = LinkedList()
linked_list.append('A')
linked_list.append('B')
linked_list.append('C')

# 링크드 리스트 데이터 출력
linked_list.print_list()  # 출력: A, B, C