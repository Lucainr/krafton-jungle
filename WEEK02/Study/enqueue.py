from collections import deque # collections 모듈에서 deque 클래스를 가져옵니다.

queue = deque() # 빈 큐(Queue)를 생성합니다.

# 삽입(Enqueue)
queue.append(1)
queue.append(2)
queue.append(3) # 큐(Queue)의 뒤에 3을 추가합니다.

print(queue)

# 삭제(Dequeue)
queue.popleft() # 큐(Queue)의 앞에서 1을 제거하고 반환합니다.

print(queue)

# 프론트(Front)
front = queue[0] # 큐(Queue)의 가장 앞에 있는 요소를 확인합니다.

print (front)
