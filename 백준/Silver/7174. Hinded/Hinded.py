import sys
input = lambda: sys.stdin.readline().rstrip()

V = int(input())
N = int(input())
ans, idx, cur = N * V, 1, 0
for i in range(1, N + 1):
    cur += int(input())
    val = cur + (N - i) * V
    if val > ans:
        ans = val
        idx = i + 1
print(ans, idx)