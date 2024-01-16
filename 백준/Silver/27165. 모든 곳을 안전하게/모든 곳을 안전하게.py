import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
a = g()
x = int(input())
idx = [i for i in range(n + 1) if a[i] == 1]
buf = []
ans = "NO"
if len(idx) == 2:
    if idx[1] - idx[0] == x:
        ans = "YES"
        buf = idx
elif len(idx) == 1:
    if idx[0] + x <= n and a[idx[0] + x]:
        ans = "YES"
        buf = [idx[0], idx[0] + x]
    elif idx[0] - x >= 0 and a[idx[0] - x] > 2:
        ans = "YES"
        buf = [idx[0] - x, idx[0]]
elif len(idx) == 0:
    for i in range(n + 1 - x):
        if a[i] > 2 and a[i + x]:
            ans = "YES"
            buf = [i, i + x]
            break
print(ans)
if ans == "YES":
    print(*buf)