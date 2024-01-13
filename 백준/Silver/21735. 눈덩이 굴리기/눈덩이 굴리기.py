import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
a = g()
ans = 0
def solve(idx, cnt, snowball):
    global ans
    ans = max(ans, snowball)
    if cnt == M:
        return
    if idx + 1 < N:
        solve(idx + 1, cnt + 1, snowball + a[idx + 1])
    if idx + 2 < N:
        solve(idx + 2, cnt + 1, snowball // 2 + a[idx + 2])
solve(-1, 0, 1)
print(ans)