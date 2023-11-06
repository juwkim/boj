import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

h, w = g()
cnt = 0
for _ in range(h):
    cnt += input().count('0')
ans = min(cnt, h * w - cnt)
print(ans)