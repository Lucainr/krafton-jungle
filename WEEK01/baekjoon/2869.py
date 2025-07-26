import math

A, B, V = map(int, input().split())

# 올라가야 하는 마지막 전날까지의 높이
need = V - A

# 하루에 올라가는 순수 거리
daily = A - B

# 반복 일수 계산 (올림 처리)
if need % daily == 0:
    days = need // daily
else:
    days = need // daily + 1

# 마지막 날 더하기
print(days + 1)