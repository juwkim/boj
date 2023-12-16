import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

l, r = g()
ans = 0
for i in range(1, 19):
    for j in range(1, 10):
        p = int(str(j) * i)
        ans += l <= p <= r
print(ans)