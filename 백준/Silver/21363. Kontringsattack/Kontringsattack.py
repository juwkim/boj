import sys
input = sys.stdin.readline

l = 1000000
N = int(input())
diff = [0] * (l + 1)
for _ in range(N):
    F, S = map(int, input().split())
    diff[abs(F - S)] += (F > S) - (F < S)
ans = 0, -l
cur = 0
for i in range(l, 0, -1):
    cur += diff[i]
    ans = max(ans, (cur, -i + 1))
print(-ans[1])