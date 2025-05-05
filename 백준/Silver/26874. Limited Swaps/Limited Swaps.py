import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

n = int(input())
a = g()
b = g()
pos = [0] * (n + 1)
for i in range(n):
    pos[b[i]] = i
res = []
for i in range(n):
    for j in range(n - 1, 0, -1):
        if pos[a[j]] < pos[a[j - 1]] and abs(a[j] - a[j - 1]) >= 2:
            a[j], a[j - 1] = a[j - 1], a[j]
            res.append(j)
if a == b:
    print(len(res))
    print(*res)
else:
    print(-1)