import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
cur = 0
for v in reversed(g()):
    if cur < v:
        cur = v
    else:
        q, r = divmod(cur, v)
        if r == 0:
            continue
        cur = (q + 1) * v
print(cur)