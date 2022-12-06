import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

t, x, m = g()
Min = 1e9
for _ in range(m):
    d, s = g()
    Min = min(Min, (d - 1) // s)
if Min == 0:
    ans = 0
elif t > Min:
    ans = Min + (t - Min) // 2
else:
    ans = t
print(ans * x)