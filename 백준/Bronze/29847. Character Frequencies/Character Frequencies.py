from collections import Counter

cnt = Counter()
for _ in range(int(input())):cnt.update(input())
del cnt['\n'], cnt[' ']
for k, v in cnt.items():
    print(k, v)