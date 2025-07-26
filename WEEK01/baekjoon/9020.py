def prime(num):
    if num ==1:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

test_case = int(input())

for _ in range(test_case):
    num = int(input())
    
    a = num//2
    b = num//2
    
    for _ in range(num//2):
        if prime(a) and prime(b):
            print(a, b)
            break
        else:
            a-=1
            b+=1
    