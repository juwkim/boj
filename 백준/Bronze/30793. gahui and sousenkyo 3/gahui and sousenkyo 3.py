import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

p, r = g()
v = p / r
if v < 0.2:
    ans = "weak"
elif v < 0.4:
    ans = "normal"
elif v < 0.6:
    ans = "strong"
else:
    ans = "very strong"
print(ans)