import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

ans, cur = 0, 0
for _ in range(int(input())):
    M, T = g()
    if T == 0:
        continue
    ans = max(ans, M - cur)
    cur = M
print(ans)