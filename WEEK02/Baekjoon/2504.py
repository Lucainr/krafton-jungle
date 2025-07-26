arr = input()          # 입력 문자열
stack = []             # 괄호를 추적할 스택
answer = 0             # 최종 결과값
tmp = 1                # 계산 중간값(곱셈용)

for i in range(len(arr)): # 각 문자를 하나씩 순회하면서 처리
    if arr[i] =='(':         # 스택에 '(' 추가
        stack.append(arr[i]) # 괄호가 열릴 때마다 2를 곱함
        tmp *=2
    elif arr[i] == '[':      # 스택에 '[' 추가
        stack.append(arr[i]) # 괄호가 열릴 때마다 3을 곱함
        tmp *=3
        
        # 괄호가 열릴수록 중첩되므로 tmp는 깊이를 반영하기 위해 계속 곱해진다.
        # ex) "([[" 이면 tmp = 2 * 3 * 3 = 18
        
    elif arr[i] == ")":
        if not stack or stack[-1] == "[": # 스택이 비었거나 잘못된 쌍
            answer = 0 # 실패
            break
        
        # stack이 비었거나 top이 '['d이면 잘못된 괄호구조니까 0을 출력하고 종료
        
        if arr[i-1] == "(": # 바로 전 괄호가 '(' 면 올바른 쌍
            answer += tmp   # 괄호가 닫히면 tmp 되돌리기
        stack.pop()         # 짝을 맞춘 괄호를 제거
        tmp //= 2  #tmp 초기화
        # 괄호를 닫았기 때문에 tmp 값을 되돌림(중첩 계산 끝남)
    else:
        if not stack or stack[-1] == "(": # 오류 상황
            answer=0
            break
        if arr[i-1] =='[': # 바로 전이 '['이면 유효
            answer+=tmp
        stack.pop()
        tmp //=3 #tmp 초기화
        # arr[i-1] =='['일 때만 []로 판단해 tmp를 더함
        # 이후 괄호의 짝을 제거하고 tmp를 3으로 나눠 되돌림

if stack:
    print(0)
else:
    print(answer)
    # 스택에 남아있으면 -> 여는 괄호가 남은 것이니 잘못된 구조.
    # 정상 종료 -> 계산된 answer 출력