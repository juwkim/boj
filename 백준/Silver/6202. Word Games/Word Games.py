from collections import Counter
N, D = tuple(map(int, input().split()))
cnt = Counter(input())
for word in map(str.rstrip, open('scrbl.txt')):
    left = 0
    word_cnt = Counter(word)
    for key in word_cnt:
        left += max(0, word_cnt[key] - cnt[key])
    if left <= cnt['#']:
        print(word)