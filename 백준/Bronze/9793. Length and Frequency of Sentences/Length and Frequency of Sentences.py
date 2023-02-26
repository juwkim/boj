from collections import Counter

cnt = Counter()
for _ in range(int(input())):
    cnt[len(input().split())] += 1
for key in sorted(cnt.keys()):
    print(key, cnt[key])