from collections import deque

# 맨 앞의 요소 확인(Peek)
def peek(queue):
    if len(queue) > 0: # 큐(Queue)의 길이가 0 보다 큰 경우
        return queue[0] # 큐(Queue)의 맨 앞 요소를 반환합니다.
    else:
        return "Queue is empty" # 큐가 비어 있으면 메세지를 변환합니다.

queue = deque()

# for i in range(1, 5+1):
#     queue.append(i)

print(peek(queue)) # 출력 : 5