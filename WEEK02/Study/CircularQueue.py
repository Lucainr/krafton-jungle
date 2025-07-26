from collections import deque

class CircularQueue:
    def __init__(self, size):
        self.size = size # 큐의 크기를 설정합니다.
        self.queue = [None] * size # 크기만큼의 리스트를 생성하여 큐를 초기화 합니다.
        self.front = self.rear = -1 # front와 rear를 초기화합니다.
        
    def is_full(self):
        # rear 다음 위치가 front인 경우 큐가 가득 찬 상태입니다.
        return (self.rear + 1) % self.size == self.front
    
    
# 사용 예제
cq = CircularQueue(3) # 크기가 3인 환형 큐(Queue)를 생성합니다.
print(cq.is_full()) # 출력 : False


