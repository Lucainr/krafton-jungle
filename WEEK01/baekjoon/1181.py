import sys

cnt = int(sys.stdin.readline())

word_list = []

for _ in range(cnt):
    word_list.append(sys.stdin.readline().strip())

word_list = list(set(word_list))

word_list.sort(key=lambda x: (len(x), x))

for word in word_list:
    print(word)