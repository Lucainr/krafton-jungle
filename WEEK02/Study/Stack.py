from queue import LifoQueue

# LifoQueue 객체 생성
stack = LifoQueue()

# 데이터 추가 (push)
stack.put(1)
stack.put(2)
stack.put(3)

# 스택의 크기 확인
print("스택의 크기:", stack.qsize())

# 데이터 제거 및 반환 (pop)
print("pop:", stack.get())

# 스택의 크기 다시 확인
print("스택의 크기:", stack.qsize())

# peek 기능 구현 (맨 위 데이터 확인)
def peek(stack):
    if not stack.empty():
        top_element = stack.get()
        stack.put(top_element)
        return top_element
    else:
        raise IndexError("peek from empty stack")

# peek 함수 사용 예제
print("peek:", peek(stack))

# 스택의 크기 확인 (peek 함수는 데이터를 제거하지 않음)
print("스택의 크기:", stack.qsize())