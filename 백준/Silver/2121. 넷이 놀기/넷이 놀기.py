import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: tuple(map(int, input().split()))

N = int(input())
A, B = g()
points = set(g() for _ in range(N))
ans = 0
for x, y in points:
    if (x + A, y) in points and (x, y + B) in points and (x + A, y + B) in points:
        ans += 1
print(ans)