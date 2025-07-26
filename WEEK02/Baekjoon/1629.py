# 자연수 A를 B번 곱한 후 C로 나눈 나머지를 알고 싶다.

import sys

input = sys.stdin.readline

def reduce_pow(a, b, c):
    if b == 1:
        return a % c
    
    x = reduce_pow(a, b//2, c)
    
    if b % 2 == 0:
        return (x * x) % c    
    else:
        return a * (x * x) % c

a, b, c= map(int, input().split())

print(reduce_pow(a, b, c))