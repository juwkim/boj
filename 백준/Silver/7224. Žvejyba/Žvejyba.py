import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n, k = g()
px = [0] * (n + k)
for i, c in enumerate(input(), 1):
    px[i] = px[i - 1] + (c == 'L')
ans = max(range(n), key=lambda i: px[i + k] - px[i]) + 1
print(ans)