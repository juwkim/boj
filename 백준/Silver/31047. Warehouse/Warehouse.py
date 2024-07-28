import sys
input = sys.stdin.readline
from collections import Counter

for _ in range(int(input())):
    cnt = Counter()
    for _ in range(int(input())):
        name, c = input().split()
        cnt[name] += int(c)
    print(len(cnt))
    for name, cnt in sorted(cnt.items(), key=lambda x: (-x[1], x[0])):
        print(name, cnt)