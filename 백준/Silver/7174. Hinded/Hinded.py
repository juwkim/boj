import sys
input = lambda: sys.stdin.readline().rstrip()

V = int(input())
N = int(input())
ans, idx, cur = 0, 0, 0
for i in range(N):
    val = cur + (N - i) * V
    if val > ans:
        ans = val
        idx = i + 1
    cur += int(input())
if cur > ans:
    ans = cur
    idx = N + 1
print(ans, idx)