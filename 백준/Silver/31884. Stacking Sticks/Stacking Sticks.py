import sys
input = sys.stdin.readline
from collections import Counter

cnt = Counter()
for _ in range(int(input())):
    cmd, i = map(int, input().split())
    match cmd:
        case 1:
            h = max(cnt[i], cnt[i+1], cnt[i+2], cnt[i+3]) + 1
            for j in range(i, i + 4):
                cnt[j] = h
        case 2:
            cnt[i] += 4
        case 3:
            print(cnt[i])