import sys
g = lambda: map(int, sys.stdin.readline().split())

n, m, k = g()
ans = [0] * (m + 1)
start = [0] * (m + 1)
for _ in range(k):
    p, c = g()
    if start[c]:
        if p == start[c]:
            ans[c] += 100
        else:
            ans[c] += abs(p - start[c])
        start[c] = 0
    else:
        start[c] = p
for i in range(1, m + 1):
    if start[i]:
        ans[i] += 100
print(*ans[1:])