import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
cnt = Counter()
for _ in range(n * (n - 1) >> 1):
    A, B, *l = input().split()
    score_a, score_b = map(int, l)
    if score_a > score_b:
        cnt[A] += 3
        cnt[B] += 0
    elif score_a < score_b:
        cnt[A] += 0
        cnt[B] += 3
    else:
        cnt[A] += 1
        cnt[B] += 1
for k, v in sorted(cnt.items(), key=lambda x: (-x[1], x[0]))[:5]:
    print(k, v)