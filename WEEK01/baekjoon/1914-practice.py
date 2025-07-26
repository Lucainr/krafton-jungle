def move(no: int, x: int, y: int) -> None:
    """no개 원반을 x 기둥에서 y 기둥으로 옮김"""
    if no > 1:
        move(no - 1, x, 6 - x - y)  # Step 1: n-1개를 보조 기둥으로 옮김

    print(f'원반 [{no}]을 {x}기둥에서 {y}기둥으로 옮깁니다')  # Step 2: 가장 큰 원반 옮김

    if no > 1:
        move(no - 1, 6 - x - y, y)  # Step 3: 보조 기둥에 있는 n-1개를 목표 기둥으로 옮김
print('하노이의 탑을 구현합니다.') 
n = int(input('원판 개수 입력'))

move(n, 1, 3)   
