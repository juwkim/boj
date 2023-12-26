import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

t, s = g()
ans = 0
for _ in range(int(input())):
    a, b = g()
    if a > b:
        continue
    if b < t:
        continue
    if a < t:
        a = t
    q1, r1 = divmod(a - 1 - t + s, s)
    q2, r2 = divmod(b - t + s, s)
    ans += q2 - q1
print(ans)