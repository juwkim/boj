import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

n = int(input())
a = g()
ans = 0
for i in range(n):
    x, y = g()
    if a[i]:
        ans += max(0, y - x)
print(ans)