import collections

# 연결 리스트의 노드를 정의하는 클래스
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key        # 키
        self.value = value    # 값
        self.next = None      # 다음 노드를 가리키는 포인터 (기본은 None)

class MyHashMap:
    # 초기화 메서드
    def __init__(self):
        self.size = 1000  # 해시맵 크기 설정 (충돌을 줄이기 위한 크기)
        # 각 해시 인덱스 위치에 ListNode를 기본값으로 갖는 딕셔너리
        self.table = collections.defaultdict(ListNode)

    # put(key, value): 키-값 쌍을 해시맵에 삽입하거나 값 업데이트
    def put(self, key, value):
        index = key % self.size  # 해시 함수: 키를 나눠 인덱스를 계산

        # 인덱스에 노드가 없는 경우 (defaultdict는 빈 ListNode로 초기화됨)
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)  # 바로 삽입
            return

        # 인덱스에 노드가 이미 있는 경우: 연결 리스트를 따라가며 처리
        p = self.table[index]
        while p:
            if p.key == key:
                # 동일한 키가 존재하면 값만 갱신하고 종료
                p.value = value
                return
            if p.next is None:
                break  # 마지막 노드까지 왔으면 반복 종료
            p = p.next
        # 키가 없었으므로 마지막에 새 노드 추가
        p.next = ListNode(key, value)

    # get(key): 키에 해당하는 값을 반환 (없으면 -1 반환)
    def get(self, key):
        index = key % self.size  # 해시 함수로 인덱스 계산

        # 인덱스에 노드가 존재하지 않는 경우
        if self.table[index].value is None:
            return -1

        # 연결 리스트를 따라가며 키를 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value  # 키가 일치하면 값 반환
            p = p.next

        return -1  # 끝까지 가도 키가 없으면 -1

    # remove(key): 해시맵에서 해당 키 제거
    def remove(self, key):
        index = key % self.size  # 해시 함수로 인덱스 계산

        # 인덱스에 노드가 없으면 제거할 것도 없음
        if self.table[index].value is None:
            return

        p = self.table[index]
        # 첫 번째 노드가 삭제 대상일 경우
        if p.key == key:
            # 다음 노드가 없으면 빈 노드로 대체, 있으면 다음 노드를 첫 노드로
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 첫 번째가 아닌 경우: 이전 노드(prev)를 이용해 연결 끊기
        prev = p
        p = p.next
        while p:
            if p.key == key:
                prev.next = p.next  # 현재 노드를 제거하고 이전 노드를 다음 노드로 연결
                return
            prev, p = p, p.next  # 한 칸 앞으로 이동