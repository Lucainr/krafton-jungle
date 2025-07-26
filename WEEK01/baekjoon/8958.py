n = int(input())

for _ in range(n):
    quiz = input().strip()
    score = 0
    cnt = 0

    for ans in quiz:
        if ans == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0

    print(score)