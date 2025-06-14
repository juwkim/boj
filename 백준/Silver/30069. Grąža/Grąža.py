import sys
input = sys.stdin.readline
from collections import Counter

cnt = Counter()
for _ in range(int(input())):
    t = int(input())
    if t > 0:
        cnt[t] += 1
    else:
        amount = -t
        result = []
        for d in (1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1):
            q = min(cnt[d], amount // d)
            amount -= q * d
            cnt[d] -= q
            result.extend([d] * q)
            if amount == 0:
                break
        print(*result)