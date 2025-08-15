import sys
input = sys.stdin.readline

l = 1000000
d = [0] * (l + 1)
for _ in range(int(input())):
    F, S = map(int, input().split())
    d[abs(F - S)] += (F > S) - (F < S)
ans = 0, -l
cur = 0
for i in range(l, 0, -1):
    cur += d[i]
    ans = max(ans, (cur, 1 - i))
print(-ans[1])