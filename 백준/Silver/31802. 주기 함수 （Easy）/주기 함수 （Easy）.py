import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

p = int(input())
px = [0] * (p + 1)
for i, num in enumerate(g()):
    px[i + 1] = px[i] + num
a, b = g()
q1, r1 = divmod(a, p)
q2, r2 = divmod(b, p)
print(px[p] * (q2 - q1) + px[r2] - px[r1])