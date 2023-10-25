import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import defaultdict

weight = [100, 75, 60, 50, 45, 40, 36, 32, 29, 26, 24, 22, 20, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

n = int(input())
cnt = defaultdict(int)
buf = []
for i in range(n):
    s, p, f, o = g()
    key = (-s, p, f)
    buf.append((key, o, i))
    cnt[key] += 1
buf.sort()

score = {}
for r, (key, o, i) in enumerate(buf):
    if key in score:
        continue
    score[key] = (sum(weight[r:r + cnt[key]]) + cnt[key] - 1) // cnt[key]

ans = [-1] * n
for key, o, i in buf:
    ans[i] = score[key] + o
print(*ans, sep='\n')