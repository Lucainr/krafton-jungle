from collections import deque

queue = deque()

queue.append(1)

# 큐의 크기 확인(Size)
queue_size = len(queue) # 큐의 현재 크기를 반환합니다.
print(queue_size) # 출력 : 1