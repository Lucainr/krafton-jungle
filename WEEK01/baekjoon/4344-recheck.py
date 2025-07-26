test_cnt = int(input())

for _ in range(test_cnt):
    data = list(map(int, input().split()))
    N = data[0]
    scores = data[1:]

    avg = sum(scores) / N

    cnt = 0
    for score in scores:
        if score > avg:
            cnt += 1

    ratio = (cnt / N) * 100
    print(f"{ratio:.3f}%")