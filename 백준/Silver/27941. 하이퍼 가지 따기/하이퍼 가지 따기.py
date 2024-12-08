from collections import Counter

cnt = [Counter() for _ in range(11)]
for l in open(0):
    for i, c in enumerate(l.split()):
        cnt[i][c] += 1
for i in range(11):
    for k, v in sorted(cnt[i].items()):
        if v == 1023:
            print(k, end=' ')
            break