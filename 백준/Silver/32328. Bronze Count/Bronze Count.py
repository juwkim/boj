from collections import Counter

cnt = Counter(int(input()) for _ in range(int(input())))
k = sorted(cnt)[-3]
v = cnt[k]
print(k, v)