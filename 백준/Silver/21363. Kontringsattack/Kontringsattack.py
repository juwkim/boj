import sys
input = sys.stdin.readline

N = int(input())
diff = [0] * 1000001
for _ in range(N):
    F, S = map(int, input().split())
    diff[abs(F - S)] += (F > S) - (F < S)
ans = 0, -1000001
cur = 0
for i in range(1000000, 0, -1):
    cur += diff[i]
    ans = max(ans, (cur, -i))
print(-ans[1] - 1)