test_cnt = int(input())

for _ in range(test_cnt):
    a, b = input().split()
    cnt = int(a)
    text = ""
    for spell in b:
        text += spell * cnt
    print(text)